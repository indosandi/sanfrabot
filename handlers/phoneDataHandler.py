import logging

from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler

logger = logging.getLogger()
class PhoneDataHandler(DataHandler):

    def handleData(self, bot, message, response):
        phone_number=message.contact.phone_number
        userKey=message.chat.id
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.no=phone_number
            # print('phone handler exist')
        else:
            userdata=UserData()
            userdata.no=phone_number
            # print('phone handler not exist',phone_number)
        try:
            self.dbconnector.save(userKey,userdata)
            logger.info("phone data is saved to db")
        except Exception as e:
            logger.error("fail save phone data")
