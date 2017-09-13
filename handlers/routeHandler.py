from handler.dataHandler import DataHandler
class RouteHandler(DataHandler):

    KEY='state'

    def getState(self,chatId):
        userKey=str(chatId)+RouteHandler.KEY
        if self.dbconnector.keyExist(userKey):
            return self.dbconnector.read(userKey)
        else:
            return None

    def setState(self,chatId,stateName):
        userKey=str(chatId)+RouteHandler.KEY
        self.dbconnector.save(userKey,stateName)