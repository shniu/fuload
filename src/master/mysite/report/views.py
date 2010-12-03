try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse
from django.shortcuts import render_to_response

from report_handler import ReportHandler

def HandleReportUpload(request,masterId):
    #if request.method != 'POST':
        #return HttpResponse(json.dumps({"ret":-1,"msg":"please use post method"}))

    if 'reportinfo' not in request.POST:
        return HttpResponse(json.dumps({"ret":-1,"msg":"no reportinfo in postdata"}))

    slaveReport = request.POST['reportinfo'];

    handler = ReportHandler()
    ret = handler.set_report(int(masterId), slaveReport)
    if ret is False:
        return HttpResponse(json.dumps({"ret":-1,"msg":"set_report failed"}))
    return HttpResponse(json.dumps({"ret":0}))
