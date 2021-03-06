#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        comm_def.py
#  Description:     定义的一些全局参数
#  Version:         1.0
#  LastChange:      2010-12-25 23:19:50
#  History:         
#=============================================================================
'''

#五分钟
split_minutes = 5

#显示饼图的最大分类数
pie_colors = ('004CB0','EC0033','FF7300','999999','00B869','FFCD00','A0D300')

#X轴最大的长度
max_x_len = 96

#flash默认宽度
default_grid_width = 900

#flash y,x默认比例
default_persent_yx = 175

#展示数据时，前台传来的rtype与attr，name等的对应
rtype2attr = {
        'allavgnum':{
            'attr':'allAvgNum',
            'showhandler':'ReportShowLineHandler',
            'name':'总每秒调用量',
            'accuracy':'%.2f',
            'order':0,
            },
        'sucavgnum':{
            'attr':'sucAvgNum',
            'showhandler':'ReportShowLineHandler',
            'name':'成功每秒调用量',
            'accuracy':'%.2f',
            'order':1,
            },
        'erravgnum':{
            'attr':'errAvgNum',
            'showhandler':'ReportShowLineHandler',
            'name':'失败每秒调用量',
            'accuracy':'%.2f',
            'order':2,
            },

        'allavgtime':{
            'attr':'allAvgTime',
            'showhandler':'ReportShowLineHandler',
            'name':'总平均响应时间(ms)',
            'accuracy':'%.2f',
            'order':3,
            },
        'sucavgtime':{
            'attr':'sucAvgTime',
            'showhandler':'ReportShowLineHandler',
            'name':'成功平均响应时间(ms)',
            'accuracy':'%.2f',
            'order':4,
            },
        'erravgtime':{
            'attr':'errAvgTime',
            'showhandler':'ReportShowLineHandler',
            'name':'失败平均响应时间(ms)',
            'accuracy':'%.2f',
            'order':5,
            },
        
        'sucrate':{
            'attr':'sucRate',
            'showhandler':'ReportShowLineHandler',
            'name':'成功率(%)',
            'accuracy':'%.2f',
            'order':6,
            },
        'errrate':{
            'attr':'errRate',
            'showhandler':'ReportShowLineHandler',
            'name':'失败率(%)',
            'accuracy':'%.2f',
            'order':7,
            },

        'alltimemap':{
            'attr':'alltimemap',
            'showhandler':'ReportShowPieHandler',
            'name':'总响应时间饼图(ms)',
            'accuracy':'%.2f',
            'order':8,
            },
        'suctimemap':{
            'attr':'suctimemap',
            'showhandler':'ReportShowPieHandler',
            'name':'成功响应时间饼图(ms)',
            'accuracy':'%.2f',
            'order':9,
            },
        'errtimemap':{
            'attr':'errtimemap',
            'showhandler':'ReportShowPieHandler',
            'name':'失败响应时间饼图(ms)',
            'accuracy':'%.2f',
            'order':10,
            },

        'retmap':{
            'attr':'retmap',
            'showhandler':'ReportShowPieHandler',
            'name':'返回码饼图',
            'accuracy':'%.4f',
            'order':11,
            },
        }
