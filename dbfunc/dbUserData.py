from dbfunc.dbredis import DbRedis
from dbfunc.userData import UserData
from dbfunc.orderData import OrderData
import json
import time
import datetime

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

    def readOrder(self,key):
        obj=super(DbUserData,self).read(key)
        return OrderData.de_json(obj)

    def saveOrder(self,key,orderdata):
        dic=orderdata.toJsonUserData()
        super(DbUserData,self).save(key,json.dumps(dic))

    def setReadyOrder(self,key):

        # create new order

        # read driver data
        userdata = self.read(key)

        tipe=userdata.ojek
        harga=userdata.harga
        dari=userdata.dari
        ke=userdata.ke
        sourceUser=key
        timestamp=int(time.time())
        dateTime=datetime.datetime.fromtimestamp(timestamp).strftime('%y%m%d%H%M%S')
        idOrder=dateTime
        # idOrder=int(timestamp%1000)/10

        orderData=OrderData()
        orderData.userSource=sourceUser
        orderData.hargaPassenger=harga
        orderData.timestamp=timestamp
        orderData.dari=dari
        orderData.ke=ke
        orderData.tipe=tipe
        orderData.status=DbUserData.STATUS_OPEN

        keyOrder=key+'Ord'+str(idOrder)
        keyUserOrder=key+'Order'
        orderData.id=keyOrder
        orderData.hargaDriver=keyOrder+'hdriv'

        #execute
        try:
            self.save(keyOrder,orderData)
            query="SET"+' '+keyUserOrder+' '+keyOrder
            self.dbcon.execute_command(query)
            logger.info("order data is saved to db")
            query="SADD "+orderData.hargaDriver+' '+'test'
            self.dbcon.execute_command(query)
        except Exception as e:
            logger.error("fail order data ")
            logger.error(str(e))
        return self.getRadius(orderData),orderData

    def remove(self,key):
        # read driver data
        orderData=None
        orderValue=None
        try:
            query='GET '+key+'Order'
            orderValue=self.dbcon.execute_command(query)
            orderData= self.readOrder(orderValue)
        except Exception as e:
            logger.error("fail reloading user order data ")
            logger.error(str(e))

        if (orderData.status==DbUserData.STATUS_OPEN):
            orderData.status = DbUserData.STATUS_CLOSED
            orderData.timefilled=int(time.time()*1000)

            #execute
            try:
                self.save(orderValue,orderData)
                logger.info("order data is saved to db")
            except Exception as e:
                logger.error("fail order data ")
                logger.error(str(e))


    def getRadius(self,order):
        tipe=order.tipe
        lat=order.dari['location']['latitude']
        lng=order.dari['location']['longitude']
        query='GEORADIUS '+str(tipe)+' '+str(lng)+' '+str(lat)+' '+'2 km WITHDIST ASC'
        out=None
        try:
            out=self.dbcon.execute_command(query)
        except Exception as e:
            logger.error("fail get radius")
            logger.error(str(e))
        if out is None:
            return []
        else:
            return out

