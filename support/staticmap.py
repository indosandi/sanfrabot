
import os
import logging
logger = logging.getLogger()
api=os.environ['GSTATICMAP']
def genUrl(coord,marker):
    lat=coord['lat']
    lng=coord['lng']
    mrkStr=getMarkerStr(marker)
    url='https://maps.googleapis.com/maps/api/staticmap?center='+str(lat)+','+str(lng)+'&zoom=14&scale=1&size=300x300&maptype=roadmap'+mrkStr+'&key='+api
    return url


def getMarkerStr(marker):
    mrkstr=''
    for mrk in marker:
        lat=mrk['lat']
        lng=mrk['lng']
        mrkstr+='&markers=color:blue%7Clabel:P%7C'+str(lat)+','+str(lng)
    return mrkstr


