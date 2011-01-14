#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
#=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        report_show_handler.py
#  Description:     对书
#  Version:         1.0
#  LastChange:      2011-01-14 21:50:34
#  History:         
#=============================================================================
'''
import datetime

from comm_def import split_minutes,rtype2attr,max_x_len,pie_colors

class ReportShowBaseHandler(object):

    _data_file = ''
    _swf_file = ''

    #仅仅是把数据查找出来没有做进一步的处理
    def get_report_objs(self, cd):
        from models import StatDetail
        objs = StatDetail.objects.filter(reportId=cd['reportid'])

        if 'clientip' in cd and cd['clientip'] is not None:
            objs = objs.filter(clientIp=cd['clientip'])

        if 'begintime' in cd and cd['begintime'] is not None:
            objs = objs.filter(firstTime__gte=cd['begintime'])

        if 'endtime' in cd and cd['endtime'] is not None:
            objs = objs.filter(firstTime__lt=cd['endtime'])

        objs.order_by('firstTime')

        return objs

    def get_data(self, cd):
        pass

    def get_data_file(self):
        return self._data_file

    def get_swf_file(self):
        return self._swf_file

class ReportShowLineHandler(ReportShowBaseHandler):
    def __init__(self):
        super(ReportShowLineHandler, self).__init__()
        self._data_file = 'show/line_data.xml'
        self._swf_file = 'fcp-line-chart.swf'

    def get_data(self, cd):
        from models import StatDetail

        objs = self.get_report_objs(cd)

        if objs is None or len(objs) == 0:
            return []

        rtype = cd['rtype']

        begintime = objs[0].firstTime
        endtime = objs[len(objs)-1].firstTime

        data = []
        t = datetime.timedelta(minutes=split_minutes)
        d = begintime
        while d <= endtime:
            t_item= {}
            t_item['x']=d
            try:
                 obj = objs.get(firstTime=d)
            except StatDetail.DoesNotExist:
                t_item['y'] = None
            else:
                t_item['y'] = getattr(obj,rtype2attr[rtype]['attr'])
            data.append(t_item)
            d = d+t

        if cd['adjust'] == 0:
            data = self._compress_data_line(data,max_x_len)

        for item in data:
            if item['x'] is not None:
                item['x'] = item['x'].strftime('%Y-%m-%d %H:%M')
            if item['y'] is not None:
                item['y'] = rtype2attr[rtype]['accuracy'] % item['y']

        return data

    def _compress_data_line(self, data, max_len):
        '''
        压缩线性的数据
        '''
        while len(data) > max_len:
            t_data = []
            for i,item in enumerate(data):
                if i%2 == 0:
                    if i+1 < len(data):
                        first_y = item['y']
                        second_y = data[i+1]['y']
                        if first_y is not None and second_y is not None:
                            t_y = (float(first_y)+float(second_y)) / 2
                        else:
                            t_y = first_y if first_y is not None else second_y

                        t_item = {
                                'x':item['x'],
                                'y':t_y
                                }
                    else:
                        t_item = item
                    t_data.append(t_item)
            data = t_data
        return data

class ReportShowPieHandler(ReportShowBaseHandler):
    def __init__(self):
        super(ReportShowPieHandler, self).__init__()
        self._data_file = 'show/pie_data.xml'
        self._swf_file = 'fcp-pie-2d-charts.swf'

    def get_data(self, cd):
        '''
        获取饼状的数据
        '''
        objs = self.get_report_objs(cd)

        if objs is None or len(objs) == 0:
            return []
        rtype = cd['rtype']

        data_map = {}
        for obj in objs:
            report_info = eval(obj.reportInfo)
            t_map = report_info[rtype]
            if t_map is None:
                continue
            for k,v in t_map.items():
                if k in data_map:
                    data_map[k] += v
                else:
                    data_map[k] = v

        orig_data = []
        for k,v in data_map.items():
            t_item = {
                    'name':k,
                    'value':v
                    }
            orig_data.append(t_item)

        orig_data.sort(lambda x,y: cmp(y['value'], x['value']))   

        max_pie_typecount = len(pie_colors) - 1

        #截断出最大类别
        cut_data = orig_data[:max_pie_typecount]

        if len(orig_data) > max_pie_typecount:
            sum_d = 0
            for i in range(max_pie_typecount,len(orig_data)):
                sum_d += orig_data[i]['value']
            cut_data.append({'name':'else','value':sum_d})

        sum_value = 0

        for v in cut_data:
            sum_value+=v['value']

        #加上颜色
        accuracy = rtype2attr[rtype]['accuracy']
        for i,item in enumerate(cut_data):
            item['color'] = pie_colors[i]
            if float(sum_value) != 0:
                item['value'] = accuracy % (float(item['value']) * float(100) / float(sum_value))
            else:
                item['value'] = 0

        return cut_data

class ReportShowMultiLineHandler(ReportShowBaseHandler):
    def __init__(self):
        super(ReportShowMultiLineHandler, self).__init__()

    def get_data(self, cd):
        pass

def get_show_handler(swftype):
    dict_swftype = {
            'line':ReportShowLineHandler,
            'pie':ReportShowPieHandler,
    }
    if swftype in dict_swftype:
        return dict_swftype[swftype]()
    else:
        raise TypeError