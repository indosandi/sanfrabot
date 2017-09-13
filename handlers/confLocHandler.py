import logging

from dbfunc.userData import UserData
from locationDataHandler import LocationDataHandler
import traceback

logger = logging.getLogger()

class ConfLocDataHandler(LocationDataHandler):

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
                traceback.print_exc()
            if self.dbconnector.keyExist(userKey):
                userdata=self.dbconnector.read(userKey)
                userdata.dari=userdataTemp.dari
            else:
                userdata=UserData()
                userdata.dari=userdataTemp.dari
            self.dbconnector.save(userKey,userdata)