import logging

from locationDataHandler import LocationDataHandler
from dbfunc.userData import UserData

logger = logging.getLogger()

class KeDataHandler(LocationDataHandler):
    def dbhandler(self, bot, message, venue, response):
        userKey = str(message.chat.id) + 'locationTemp'
        userdata = None
        if self.dbconnector.keyExist(userKey):
            userdata = self.dbconnector.read(userKey)
            userdata.setKe(venue)
            # userdata.ke= venue
        else:
            userdata = UserData()
            userdata.setKe(venue)
            # userdata.ke= venue
        self.dbconnector.save(userKey, userdata)