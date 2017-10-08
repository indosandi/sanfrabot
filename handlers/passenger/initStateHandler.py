from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler


class InitStateHandler(DataHandler):

    def handleData(self, bot, message, response):
        userKey=message.chat.id
        userData=None
        if self.dbconnector.keyExist(userKey):
            userData=self.dbconnector.read(userKey)
        else:
            userData=UserData(msg=message)
            self.dbconnector.save(userKey,userData)
        response.addText(userData.toString())


