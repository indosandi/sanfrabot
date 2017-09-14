import logging
import time
from locationDataHandler import LocationDataHandler
from dbfunc.userData import UserData

logger = logging.getLogger()

class DariDataHandler(LocationDataHandler):
    def dbhandler(self, bot, message,  venue, response):
        userKey=str(message.chat.id)+'locationTemp'
        userdata=None
        if self.dbconnector.keyExist(userKey):
            userdata=self.dbconnector.read(userKey)
            userdata.dari=venue
        else:
            userdata=UserData()
            userdata.dari=venue
        self.dbconnector.save(userKey,userdata)

    # def tunggu(self):
    #     for i in range(0,10):
    #         time.sleep(1)
    #         print(i)