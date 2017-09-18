import logging

from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler

logger = logging.getLogger()
class DriverPhone(DataHandler):

    def handleData(self, bot, message, response):
        phone_number=self.addPlus(message.contact.phone_number)
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
            driverdata.no=phone_number
        else:
            userdata=DriverData()
            userdata.no=phone_number
        try:
            self.dbconnector.save(userKey,driverdata)
            logger.info("driver phone data is saved to db")
        except Exception as e:
            logger.error("fail save phone data")

    def addPlus(self,phone_number):
        if phone_number[0]=='+':
            return phone_number
        else:
            return '+'+phone_number

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'
