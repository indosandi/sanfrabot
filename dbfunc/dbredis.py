from dbfunc.dbfn import Dbfn
import os
import redis
class DbRedis(Dbfn):

    def __init__(self):
        self.passwd=os.environ['password']
        self.host=os.environ['redisHost']
        self.port=int(os.environ['redisPort'])
        pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.passwd)
        self.dbcon=redis.Redis(connection_pool=pool)

    def save(self,key,value):
        self.dbcon.set(key,value)

    def read(self,key):
        return self.dbcon.get(key)

    def keyExist(self,key):
        bol=self.dbcon.exists(key)
        if bol:
            return True
        else:
            return False