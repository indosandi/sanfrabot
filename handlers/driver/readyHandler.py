from handlers.dataHandler import DataHandler
from handlers.locationDataHandler import LocationDataHandler
import logging
import support.respList as respL
logger = logging.getLogger()

class ReadyHandler(DataHandler):

    def handleData(self, bot,message , response):

        userKey=self.getUserKey(message)
        driverdata = self.dbconnector.read(userKey)
        venueData = driverdata.location

        self.dbconnector.setReady(userKey)
        bot.send_message(message.chat.id,respL.updateMangkal())
        bot.send_venue(message.chat.id, venueData['location']['latitude'],venueData
        ['location']['longitude'],venueData['title'],venueData['address'] )


    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'

    def getAddress(self,key,response):
        driverdata=self.dbconnector.read(key)
        address=driverdata.location['address']
        text='current location:'+address
        response.addText(text)
