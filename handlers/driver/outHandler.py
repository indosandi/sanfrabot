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
            print('nothing should happen')

            # find what order this correspond to
            # driverId=self.getUserKey(message)
            # orderId=None
            # try:
            #     query = 'GET ' + driverId + 'nego '
            #     orderId=self.dbconnector.dbcon.execute_command(query)
            # except Exception as e:
            #     print(str(e))
            #
            # if orderId is not None:
            #     try:
            #         query = 'DEL ' + driverId + 'nego '
            #         self.dbconnector.dbcon.execute_command(query)
            #     except Exception as e:
            #         print(str(e))
            #
            #     harga=''
            #     if message.text is not None:
            #         harga=str(message.text)
            #     try:
            #         #add to set
            #         query = 'SADD ' + orderId+'hdriv'+ ' ' + driverId
            #         self.dbConDriver.dbcon.execute_command(query)
            #
            #         # set new harga to driverId
            #         query = 'SET '+driverId+'Hrg '+harga
            #         self.dbConDriver.dbcon.execute_command(query)
            #     except Exception as e:
            #         print(str(e))
            #
            #     userOrder = orderId.split('Ord')[0]
            #     bot.send_message(userOrder,text=driverId+' '+harga)
            # else:
            #     bot.send_message(driverId,text='Command salah')
            #     # add new price to hargaDriver order set
            # pass

    # def sendNewPrice(self,bot,orderId,harga):
    #     userOrder = orderId.split('Ord')[0]
    #     bot.send_message(userOrder,text=harga)

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
