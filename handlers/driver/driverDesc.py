from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler
import logging
import traceback
logger = logging.getLogger()
class DriverDesc(DataHandler):

    def handleData(self, bot,message , response):
        desc=message.text
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
            driverdata.desc=desc
        else:
            driverdata=DriverData()
            driverdata.desc=desc
        try:
            self.dbconnector.save(userKey,driverdata)
            logger.info("driver desc data is saved to db")
        except Exception as e:
            logger.error("fail desc data")
            traceback.print_exc()

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'
