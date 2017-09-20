from handlers.dataHandler import DataHandler
import logging
logger = logging.getLogger()

class OutHandler(DataHandler):

    def handleData(self, bot,message , response):
        # get driver id
        userKey=self.getUserKey(message)


        self.dbconnector.remove(userKey)

    def getUserKey(self,message):
        return str(message.chat.id)