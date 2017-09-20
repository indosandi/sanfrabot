from dbfunc.dbredis import DbRedis
from dbfunc.driverData import DriverData
import json

class DbOrder(DbRedis):

    def save(self,key,driverdata):
        dic=driverdata.toJsonUserData()
        super(DbOrder,self).save(key,json.dumps(dic))

    def read(self,key):
        obj=super(DbOrder,self).read(key)
        return DriverData.de_json(obj)

    def getDriverNearBy(self,key):
        #read current order
        ordernow=self.read(key)
        centerLat=ordernow.dari['location']['latitude']
        centerLng=ordernow.dari['location']['longitude']
        tipe=ordernow.tipe
        #query based on 2 KM radius
        # listDriver=self.dbcon

        #convert into list

        # return the list