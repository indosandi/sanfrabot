from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler


class HargaDataHandler(DataHandler):

    def handleData(self, bot,message , response):
        harga=message.text
        userKey=message.chat.id
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.harga=harga
        else:
            userdata=UserData()
            userdata.harga=harga
        self.dbconnector.save(userKey,userdata)
