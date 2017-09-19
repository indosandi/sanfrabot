from dbfunc.dbredis import DbRedis
from dbfunc.userData import UserData
from dbfunc.orderData import OrderData
import json
import time

import logging
logger = logging.getLogger()

class DbUserData(DbRedis):

    STATUS_OPEN='open'
    STATUS_CLOSED='closed'
    STATUS_FILLED='filled'
    def save(self,key,userdata):
        dic=userdata.toJsonUserData()
        super(DbUserData,self).save(key,json.dumps(dic))

    def read(self,key):
        obj=super(DbUserData,self).read(key)
        return UserData.de_json(obj)

    def setReady(self,key):

        # create new order

        # read driver data
        userdata = self.read(key)

        tipe=userdata.ojek
        harga=userdata.harga
        dari=userdata.dari
        ke=userdata.ke
        sourceUser=key
        timestamp=int(time.time()*1000)

        orderData=OrderData()
        orderData.userSource=sourceUser
        orderData.hargaPassenger=harga
        orderData.timestamp=timestamp
        orderData.dari=dari
        orderData.ke=ke
        #orderData.setDari(dari)
        #orderData.setKe(ke)
        orderData.status=DbUserData.STATUS_OPEN

        keyOrder=key+'Order'+str(timestamp)
        keyUserOrder=key+'Order'

        #execute
        try:
            self.save(keyOrder,orderData)
            self.save(keyUserOrder,keyOrder)
            logger.info("order data is saved to db")
        except Exception as e:
            logger.error("fail order data ")
            logger.error(str(e))

    def remove(self,key):
        # read driver data
        try:
            orderValue=self.read(key+'Order')
            orderData= self.read(orderValue)
        except Exception as e:
            logger.error("fail reloading user order data ")
            logger.error(str(e))

        orderData.status = DbUserData.STATUS_CLOSED
        orderData.timefilled=int(time.time()*1000)

        #execute
        try:
            self.save(key,orderData)
            logger.info("order data is saved to db")
        except Exception as e:
            logger.error("fail order data ")
            logger.error(str(e))


