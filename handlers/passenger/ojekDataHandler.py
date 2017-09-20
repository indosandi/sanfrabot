from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler
import logging

logger = logging.getLogger()
class OjekDataHandler(DataHandler):

    def handleData(self, bot, message, response):
        ojek=message.text
        userKey= self.getUserKey(message)
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.ojek=ojek
        else:
            userdata=UserData()
            userdata.ojek=ojek
        try:
            self.dbconnector.save(userKey,userdata)
            logger.info("ojek data is saved to db")
        except Exception as e:
            logger.error("fail ojek data ")
            print(str(e))

    def getUserKey(self,message):
        return str(message.chat.id)