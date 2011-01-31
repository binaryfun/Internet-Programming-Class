#!/usr/bin/python
import flickrapi
from pprint import pprint
import re
import json 

# set size of resulting images
"""
 s	small square 75x75
t	thumbnail, 100 on longest side
m	small, 240 on longest side
-	medium, 500 on longest side
z	medium 640, 640 on longest side
b	large, 1024 on longest side*
o	original image, either a jpg, gif or png, depending on source format

"""
SIZE='m' 


api_key = 'e6743a16fd4c124cf0b740a27a28b00a'

def returnPics(tag):
    """ accepts a string 'item one,tag2, tag 3't and
        returns formatted html output of images """
    flickr = flickrapi.FlickrAPI(api_key)
    photos = flickr.photos_search(tags=tag, per_page='9', format='json')

    ## For whatever reason, (perhaps that is normal????) 
    # flickr returns the response with extra stuff
    response_parser = re.match(r'jsonFlickrApi\((.*?)\)$',photos)
    response_parser=response_parser.group(1)
    pythonStyle=json.loads(response_parser)
    #print pythonStyle
    for i in range(len(pythonStyle['photos']['photo'])):
        secret=pythonStyle['photos']['photo'][i]['secret']
        farm_id = pythonStyle['photos']['photo'][i]['farm']
        server_id=pythonStyle['photos']['photo'][i]['server']
        photo_id=pythonStyle['photos']['photo'][i]['id']
        print '<img src="http://farm%s.static.flickr.com/%s/%s_%s_%s.jpg">' % (farm_id,server_id,photo_id,secret,SIZE)
        #print  farm_id,server_id,photo_id,secret,SIZE


if __name__ == '__main__':
    returnPics('buffalo new york')    
