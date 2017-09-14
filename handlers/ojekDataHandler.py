from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler


class OjekDataHandler(DataHandler):

    def handleData(self, bot, message, response):
        ojek=message.text
        userKey=message.chat.id
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.ojek=ojek
        else:
            userdata=UserData()
            userdata.ojek=ojek
        self.dbconnector.save(userKey,userdata)