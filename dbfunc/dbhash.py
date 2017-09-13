from dbfunc.dbfn import Dbfn
class Dbhash(Dbfn):

    def __init__(self):
        self.dict={}

    def save(self,key,value):
        self.dict[key]=value

    def read(self,key):
        return self.dict[key]

    def keyExist(self,key):
        if key in self.dict:
            return True
        else:
            return False