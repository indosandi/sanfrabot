from handlers.dataHandler import DataHandler
from handlers.locationDataHandler import LocationDataHandler
import logging
logger = logging.getLogger()

class OutHandler(LocationDataHandler):
# class OutHandler(DataHandler):

    def handleData(self, bot, message, response):
        #hardcoded for now
        if message.text=='Tutup':
            self.removeFromGeo(message)
        elif message.location is not None:
        # elif message.venue is not None or message.location is not None or message.text!='Tutup':
            super(OutHandler,self).handleData(bot,message,response)
        else: #expected nego harga
            logger.info('type input when not in nego')


    def dbhandler(self, bot, message, outvenue, response):
    # def handleData(self, bot,message , response):
        # get driver id
        userKey = self.getUserKey(message)
        drivedata = self.dbconnector.read(userKey)
        drivedata.setLocation(outvenue)
        self.dbconnector.save(userKey,drivedata)
        self.dbconnector.remove(userKey)

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'

    def removeFromGeo(self,message):
        userKey = self.getUserKey(message)
        self.dbconnector.remove(userKey)
