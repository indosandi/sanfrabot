import logging

from dbfunc.userData import UserData
from handlers.locationDataHandler import LocationDataHandler
import traceback
logger = logging.getLogger()

class ConfLocKeDataHandler(LocationDataHandler):

    def dbhandler(self, bot, message, venue, response):
        userKeyTemp=self.getUserKeyTemp(message)
        userKey=self.getUserKey(message)
        userdata=None
        if message.text=='yes':
            userdataTemp=None
            try:
                userdataTemp=self.dbconnector.read(userKeyTemp)
            except Exception as e:
                logger.error(str(e))
            if self.dbconnector.keyExist(userKey):
                userdata=self.dbconnector.read(userKey)
                userdata.ke=userdataTemp.ke
            else:
                userdata=UserData()
                userdata.ke=userdataTemp.ke
            try:
                self.dbconnector.save(userKey,userdata)
                logger.info("ke data conf is saved to db")
            except Exception as e:
                logger.error("fail ke data conf")
                traceback.print_exc()

    def getUserKeyTemp(self,message):
        return str(message.chat.id)+'locationTemp'

    def getUserKey(self,message):
        return str(message.chat.id)