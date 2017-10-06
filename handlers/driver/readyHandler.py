from handlers.dataHandler import DataHandler
from handlers.locationDataHandler import LocationDataHandler
import logging
logger = logging.getLogger()

class ReadyHandler(DataHandler):

    def handleData(self, bot,message , response):
    # def dbhandler(self, bot,message , outvenue, response):

        userKey=self.getUserKey(message)
        driverdata = self.dbconnector.read(userKey)
        venueData = driverdata.location
        # print(message.venue,'venue')
        # print(message.location,'location')
        # bot.send_venue(message.chat.id,message.venue.location.latitude,message.venue.location.longitude
        #                ,message.venue.title,message.venue.address)
        # if message.venue is None and message.location is None:
        self.dbconnector.setReady(userKey)
        #     venueData= driverdata.location
        bot.send_message(message.chat.id,'lokasi mangkal terbaru')
        bot.send_venue(message.chat.id, venueData['location']['latitude'],venueData
        ['location']['longitude'],venueData['title'],venueData['address'] )
        # driverdata.setLocation(outvenue)
        # address = driverdata.location['address']
        # text = 'current location:' + address
        # response.addText(text)
        # self.dbconnector.save(userKey,driverdata)
        #
        # if outvenue is not None:
        #     address = outvenue.address
        #     location = outvenue.location
        #     title = outvenue.title
        #     bot.send_venue(message.chat.id, location.latitude, location.longitude, title, address)


    # def handleData(self, bot,message , response):
    #     # get driver id
    #     userKey=self.getUserKey(message)
    #
    #
    #     self.dbconnector.setReady(userKey)
    #     self.getAddress(userKey,response)

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'

    def getAddress(self,key,response):
        driverdata=self.dbconnector.read(key)
        address=driverdata.location['address']
        text='current location:'+address
        response.addText(text)
