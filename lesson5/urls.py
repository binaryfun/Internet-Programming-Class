from django.conf.urls.defaults import *
from indexpage.views import hello,indexPrintPage,pageDetails

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^$', indexPrintPage),
    ('details', pageDetails),
)
