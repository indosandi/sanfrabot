from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler
import logging

logger = logging.getLogger()

class HargaDataHandler(DataHandler):

    def handleData(self, bot,message , response):
        harga=message.text
        userKey=self.getUserKey(message)
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.harga=harga
        else:
            userdata=UserData()
            userdata.harga=harga
        try:
            self.dbconnector.save(userKey,userdata)
            logger.info("harga data is saved to db")
        except Exception as e:
            logger.error("fail harga data ")
            print(str(e))

    def getUserKey(self,message):
        return str(message.chat.id)
