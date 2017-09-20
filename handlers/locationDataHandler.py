import logging

from handlers.dataHandler import DataHandler
from telebot.types import Location
from telebot.types import Venue
logger = logging.getLogger()
# from telegram import Venue
# from telegram import Location
import support.geocode as gserv

class LocationDataHandler(DataHandler):

    # def setRevGeoService(self,service):
    #     self.revGeoServ=service

    def handleData(self, bot, message, response):
        venue=message.venue
        location=message.location
        alamat=message.text
        outvenue=None
        logger.debug('inside handle data')

        if location is None and venue is None and alamat is not None:
            logger.debug('do geo coding')
            #get reverse geo coding from Alamat
            outgps=gserv.getLatLng(alamat)
            if outgps['lat']==gserv.errorLat and outgps['lng']==gserv.errorLng:
                outalamat=alamat+' (tidak dikenal)\n(mungkin beda di peta)'
            else:
                outalamat=alamat
            locationTemp=Location(outgps['lng'],outgps['lat'])
            outvenue=Venue(locationTemp,'',outalamat,None)
            message.venue=outvenue
        elif (venue is not None and location is not None):
            outvenue=venue
            logger.debug('venue is sent')
        elif (venue is not None and location is None):
            outvenue=venue
            logger.debug('venue is sent')
        elif (location is not None and venue is None):
            #get geocoding
            outgps=gserv.getAddress(location.latitude,location.longitude)
            outalamat='GPS:'+outgps
            outvenue=Venue(location,'',outalamat,None)
            # outvenue={'location':location,'alamat':'GPS saya'}
            # logger.info('alamat is added to location')
        elif (alamat is None and location is not None and venue is None):
            locationTemp=Location(-6.311525,106.829285)
            outvenue=Venue(locationTemp,'','tidak diketahui',None)
            # location={'latitude':-6.311525 , 'longitude':106.829285}
            # outvenue={'location':location,'alamat':'not specified'}
            logger.info('venue is synthesized')
        self.dbhandler(bot,message , outvenue, response)

    def dbhandler(self, bot,message , outvenue, response):
        pass
        # userKey=update.message.chat_id
        # userdata=None
        # if self.dbconnector.keyExist(userKey):
        #     userdata=self.dbconnector.read(userKey)
        #     userdata.location=venue
        # else:
        #     userdata=UserData()
        #     userdata.no=venue
        # self.dbconnector.save(userKey,userdata)