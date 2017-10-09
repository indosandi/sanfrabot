import logging

from handlers.locationDataHandler import LocationDataHandler
from dbfunc.userData import UserData
import traceback

logger = logging.getLogger()

class KeDataHandler(LocationDataHandler):
    def dbhandler(self, bot, message, venue, response):
        userKey = self.getUserKey(message)
        userdata = None
        if self.dbconnector.keyExist(userKey):
            userdata = self.dbconnector.read(userKey)
            userdata.setKe(venue)
            # userdata.ke= venue
        else:
            userdata = UserData()
            userdata.setKe(venue)
            # userdata.ke= venue
        try:
            self.dbconnector.save(userKey, userdata)
            logger.info("ke data is saved to db")
        except Exception as e:
            logger.error("fail ke data ")
            traceback.print_exc()

    def getUserKey(self,message):
        return str(message.chat.id) + 'locationTemp'