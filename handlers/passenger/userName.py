from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler
import logging
import traceback
logger = logging.getLogger()
class UserName(DataHandler):

    def handleData(self, bot,message , response):
        name=message.text
        userKey=self.getUserKey(message)
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.nama=name
        else:
            userdata=UserData()
            userdata.nama=name
        try:
            self.dbconnector.save(userKey,userdata)
            logger.info("user nama data is saved to db")
        except Exception as e:
            logger.error("fail save user data")
            traceback.print_exc()

    def getUserKey(self,message):
        return str(message.chat.id)
