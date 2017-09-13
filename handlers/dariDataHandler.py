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
        # logger.info(type(userdata.dari))
        # logger.info(userdata.dari)
        self.dbconnector.save(userKey,userdata)
        # print(self.dbconnector.read(userKey))
        # print('HEHEHEHE')
        location=venue.location
        title=venue.title
        address=venue.address
        # bot.send_venue(message.chat.id,location.latitude,location.longitude,title,address)
        # bot.send_location(message.chat.id,location.latitude,location.longitude)
        # bot.sendLocation(chat_id=update.message.chat_id,location=venue.location)

    # def tunggu(self):
    #     for i in range(0,10):
    #         time.sleep(1)
    #         print(i)