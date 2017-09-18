from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler
import logging
logger = logging.getLogger()
class DriverName(DataHandler):

    def handleData(self, bot,message , response):
        name=message.text
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
            driverdata.nama=name
        else:
            driverdata=DriverData()
            driverdata.nama=name
        try:
            self.dbconnector.save(userKey,driverdata)
            logger.info("driver nama data is saved to db")
        except Exception as e:
            logger.error("fail save driver data")
            print(str(e))

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'
