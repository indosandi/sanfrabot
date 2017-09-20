
class DataHandler(object):



    def __init__(self):
        self.dbconnector=None

    def setDbCon(self,dbcon):
        self.dbconnector=dbcon

    def handleData(self, bot,message , response):
        pass

    # def writeData(self,key,data):
    #     self.dbconnector.save(key,data)
    #
    # def readData(self,key):
    #     return self.dbconnector.read(key)
    #
    # def checkExist(self,key):
    #     return
