from dbfunc.dbredis import DbRedis
import dbfunc.toJson as toJson
from dbfunc.userData import UserData
import json

class DbUserData(DbRedis):

    def save(self,key,userdata):
        dic=userdata.toJsonUserData()
        # self.save(key,dic)
        print(json.dumps(dic),'json dump dic')
        super(DbUserData,self).save(key,json.dumps(dic))

    def read(self,key):
        obj=super(DbUserData,self).read(key)
        # obj= obj.replace("'", '"')
        # obj= obj.replace("None", "null")
        # print(obj,type(obj))
        return UserData.de_json(obj)

