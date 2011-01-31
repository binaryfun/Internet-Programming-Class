#!/usr/bin/python

#######################
# Aaron Bazar
# Combined two APIs (flickr and api.hostip.info)
# as asked in Assignment #3
# 01/31/11
# This program may be useful if you want to show
# site visitors pictures based on their location
#####################
import getLocation
import getRelatedPhotos
from pprint import pprint
import re


#returnLocationString(ipAddr):

def getCountry(location):
    """ extract the country name from returned string """
    m = re.match(r"Country: (.+)\(", location)
    return m.group(1)
    

def getSomePictures(ipaddr):
    """ main function. Accepts an ip address string and returns
       html-formatted list of Pictures """
    location= getLocation.returnLocationString(ipaddr)
    location=getCountry(location)
    return(getRelatedPhotos.returnPics(location))

if __name__ == '__main__':
    var = raw_input("Enter ip Address: ")
    var= var.strip()
    print getSomePictures(var)
