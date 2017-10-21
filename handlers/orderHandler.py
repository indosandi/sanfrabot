import time
import logging
from handlers.dataHandler import DataHandler
logger = logging.getLogger()
from dbfunc.orderData import OrderData

class OrderHandler(DataHandler):

    STATUS_OPEN='OPEN'
    STATUS_FILLED='FILLED'
    STATUS_CLOSED='CLOSED'

    def handleData(self, bot,message , response):
        userDataKey=str(message.chat.id)
        userKey=self.getUserKey(message)
        userdata=self.dbconnector.read(userDataKey)
        ordernow = OrderData()
        ordernow.userSource=userDataKey
        ordernow.dari=userdata.dari
        ordernow.ke=userdata.ke
        ordernow.tipe=userdata.ojek
        ordernow.hargaPassenger=userdata.harga
        ordernow.timestamp=self.timeNow()
        ordernow.status=OrderHandler.STATUS_OPEN

        try:
            self.dbOrderCon.save(userKey, ordernow)
            logger.info("order data is saved to db")
        except Exception as e:
            logger.error("fail order data conf")
            logger.error(str(e))

    def getUserKey(self, message):
        return str(message.chat.id)+'Order'+self.timeNow()

    def getUserDataKey(self,message):
        return str(message.chat.id)

    def timeNow(self):
        return str(int(time.time()*1000))

    def setOrderDbCon(self,dbcon):
        self.dbOrderCon=dbcon
