from django.http import HttpResponse
from django.shortcuts import render_to_response

import bookdb


def hello(request):
    return HttpResponse("Hello world")

# Create your views here.
###### THIS WORKS!!!!###################
#def indexPrintPage(request):
#    item_list=['item1','item2']
#    return render_to_response('index_page.html', locals())
########################################

def indexPrintPage(request):
    a=bookdb.BookDB()
    item_list = a.titles()
    return render_to_response('index_page.html', locals())

def pageDetails(request):
    id=request.get_full_path()
    id=id.replace('/details/','')
    a=bookdb.BookDB()
    item_list = a.title_info(id)
    return render_to_response('details_page.html', locals())
