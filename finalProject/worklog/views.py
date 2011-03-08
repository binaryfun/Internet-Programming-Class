from django.http import HttpResponse
from django.shortcuts import render_to_response

def printHUD(request):
    return render_to_response('index_page.html', locals())

def workLog(request):
    return render_to_response('worklog.html', locals())

