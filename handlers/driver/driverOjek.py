from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler
import logging
logger = logging.getLogger()
class DriverOjek(DataHandler):

    def handleData(self, bot,message , response):
        ojek=message.text
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
            driverdata.ojek=ojek
        else:
            driverdata=DriverData()
            driverdata.ojek=ojek
        try:
            self.dbconnector.save(userKey,driverdata)
            logger.info("driver ojek data is saved to db")
        except Exception as e:
            logger.error("fail ojek data")
            print(str(e))

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'
