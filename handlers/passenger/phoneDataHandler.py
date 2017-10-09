import logging

from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler

logger = logging.getLogger()
class PhoneDataHandler(DataHandler):

    def handleData(self, bot, message, response):
        phone_number=self.addPlus(message.contact.phone_number)
        userKey=self.getUserKey(message)
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.no=phone_number
        else:
            userdata=UserData()
            userdata.no=phone_number
        try:
            self.dbconnector.save(userKey,userdata)
            logger.info("phone data is saved to db")
        except Exception as e:
            logger.error("fail save phone data")

    def addPlus(self,phone_number):
        if phone_number[0]=='+':
            return phone_number
        else:
            return '+'+phone_number

    def getUserKey(self,message):
        return str(message.chat.id)

