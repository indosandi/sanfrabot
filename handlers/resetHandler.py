from handlers.dataHandler import DataHandler
import logging
logger = logging.getLogger()
class ResetHandler(DataHandler):

    def setDbUser(self,db):
        self.dbUser=db

    def handleData(self, bot,message , response):

        # fill order with closed status
        try:
            userKey=self.getUserKey(message)
            self.dbUser.remove(userKey)
        except Exception as e:
            logger.info('ignore the error, should only remove driver')

        # remove driver from its circle
        try:
            driverKey=self.getDriverKey(message)
            self.dbconnector.remove(driverKey)
        except Exception as e:
            logger.info('ignore the error, should only remove user')

    def getDriverKey(self,message):
        return str(message.chat.id)+'Driver'

    def getUserKey(self,message):
        return str(message.chat.id)

