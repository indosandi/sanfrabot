import logging

from dbfunc.userData import UserData
from locationDataHandler import LocationDataHandler

logger = logging.getLogger()

class ConfLocKeDataHandler(LocationDataHandler):

    def dbhandler(self, bot, message, venue, response):
        userKeyTemp=str(message.chat.id)+'locationTemp'
        userKey=message.chat.id
        userdata=None
        if message.text=='yes':
            userdataTemp=None
            try:
                userdataTemp=self.dbconnector.read(userKeyTemp)
                print(userdataTemp)
            except Exception as e:
                logger.error(str(e))
            if self.dbconnector.keyExist(userKey):
                userdata=self.dbconnector.read(userKey)
                userdata.ke=userdataTemp.ke
            else:
                userdata=UserData()
                userdata.ke=userdataTemp.ke
            self.dbconnector.save(userKey,userdata)