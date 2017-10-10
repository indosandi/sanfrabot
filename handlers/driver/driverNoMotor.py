from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler
import logging
import traceback
logger = logging.getLogger()
class DriverNoMotor(DataHandler):

    def handleData(self, bot,message , response):
        noMotor=message.text
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
            driverdata.noMotor=noMotor
        else:
            driverdata=DriverData()
            driverdata.noMotor=noMotor
        try:
            self.dbconnector.save(userKey,driverdata)
            logger.info("driver no motor data is saved to db")
        except Exception as e:
            logger.error("fail save no motor data")
            traceback.print_exc()

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'
