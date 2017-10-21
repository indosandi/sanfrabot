from telebot.types import Venue
from telebot.types import Location


def toJson(data):
    if (isinstance(data,Venue)):
        return toJsonVenue(data)
    elif (isinstance(data,Location)):
        return toJsonLocation(data)
    else:
        return None


def toJsonLocation(data):
    dic={}
    if data is not None:
        dic['latitude']=ifNone(data.latitude)
        dic['longitude']=ifNone(data.longitude)
    else:
        dic['latitude']=None
        dic['longitude']=None
    return dic


def toJsonVenue(data):
    dic={}
    if data is not None:
        dic['location']=ifNone(toJsonLocation(data.location))
        dic['title']=ifNone(data.title)
        dic['address']=ifNone(data.address)
        dic['foursquare_id']=ifNone(data.foursquare_id)
    else:
        dic['location']=None
        dic['title']=None
        dic['address']=None
        dic['foursquare_id']=None
    return dic

def ifNone(data):
    if data is None:
        return None
    else:
        return data


