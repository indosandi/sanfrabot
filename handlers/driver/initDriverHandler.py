from dbfunc.driverData import DriverData
from handlers.dataHandler import DataHandler
import logging
import support.emojis as emo
logger = logging.getLogger()

class InitDriverHandler(DataHandler):

    def handleData(self, bot, message, response):
        userKey=self.getUserKey(message)
        driverdata=None
        if self.dbconnector.keyExist(userKey):
            driverdata=self.dbconnector.read(userKey)
        else:
            driverdata=DriverData(msg=message)
            try:
                self.dbconnector.save(userKey,driverdata)
                logger.info("driver status data is saved to db")
            except Exception as e:
                logger.error("fail driver status data")
        response.addText(driverdata.toString())

    def getUserKey(self, message):
        return str(message.chat.id) + 'Driver'

