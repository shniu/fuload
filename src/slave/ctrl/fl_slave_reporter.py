#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        fl_slave_reporter.py
#  Description:     向master的上报类
#  Version:         1.0
#  LastChange:      2010-12-13 11:37:19
#  History:         
#=============================================================================
'''
import urllib
import urllib2
import logging
import traceback

try:
    import json
except ImportError:
    import simplejson as json

class SlaveReporter(object):
    _reportUrl= ""

    def __init__(self, reportUrl):
        self._reportUrl = reportUrl

    def report(self,data):
        #logging.error(data)
        req = urllib2.Request(self._reportUrl)
        #req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        #req.add_header('Connection','Keep-Alive')
        params = {"reportinfo":data}
        en_params = urllib.urlencode(params)
        try:
            readdata = urllib2.urlopen(req,en_params).read()
            obj = json.loads(readdata)
            if obj['ret'] != 0:
                logging.error("report error,ret:%d,msg:%s",obj['ret'],obj['msg'])
                return False
        except Exception, ex:
            logging.error("urllib2 exception:"+ repr(ex) + traceback.format_exc() + ",data:" +data)
            return False
        else:
            return True
