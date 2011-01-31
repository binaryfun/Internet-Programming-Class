#!/usr/bin/python
import urllib


API_URL='http://api.hostip.info/get_html.php?ip='

#################
#http://api.hostip.info/get_html.php?ip=69.99.171.145
#############################
#>>> import urllib
#>>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
#>>> f = urllib.urlopen("http://abc.com/query?%s" % params)
#>>> print f.read()
#####################

def returnLocationString(ipAddr):
    f=urllib.urlopen((API_URL+ipAddr))
    return f.read()

if __name__ == '__main__':
    print returnLocationString('69.99.171.145')
