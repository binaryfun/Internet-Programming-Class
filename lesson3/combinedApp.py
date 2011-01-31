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
        list of Pictures """

    location= getLocation.returnLocationString(ipaddr)
    location=getCountry(location)
    return(getRelatedPhotos.returnPics(location))

if __name__ == '__main__':
    var = raw_input("Enter ip Address: ")
    var= var.strip()
    print getSomePictures(var)
