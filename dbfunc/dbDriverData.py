from dbfunc.dbredis import DbRedis
from dbfunc.driverData import DriverData
import json
import logging
logger = logging.getLogger()

class DbDriverData(DbRedis):

    def save(self,key,driverdata):
        dic=driverdata.toJsonUserData()
        super(DbDriverData,self).save(key,json.dumps(dic))

    def read(self,key):
        obj=super(DbDriverData,self).read(key)
        return DriverData.de_json(obj)

    def setReady(self,key):
        #add driver to corresponding location

        # read driver data
        driverdata= self.read(key)

        # name of location is tipe
        tipe=driverdata.ojek

        # driver id is key
        driverId= key

        # read lat lng
        lat= driverdata.location['location']['latitude']
        lng= driverdata.location['location']['longitude']

        # create query
        # GEOADD tipe lat lng driverId
        query="GEOADD"+' '+str(tipe)+' '+str(lng)+' '+str(lat)+' '+driverId
        print(query)

        #execute
        try:
            self.dbcon.execute_command(query)
            logger.info("order driver data is saved to db")
        except Exception as e:
            logger.error("fail order driver data ")
            logger.error(str(e))

    def remove(self,key):
        # read driver data
        driverdata = self.read(key)

        driverId = key

        # name of location is tipe
        tipe = driverdata.ojek

        #query
        query = 'ZREM '+tipe+' '+driverId

        #execute
        try:
            self.dbcon.execute_command(query)
            logger.info("order driver data is removed from db")
        except Exception as e:
            logger.error("fail removing order driver data ")
            logger.error(str(e))
