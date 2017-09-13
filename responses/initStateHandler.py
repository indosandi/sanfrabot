from dbfunc.userData import UserData
from handlers.dataHandler import DataHandler


class InitStateHandler(DataHandler):

    def handleData(self, bot, message, response):
        userKey=message.chat.id
        userData=None
        if self.dbconnector.keyExist(userKey):
            userData=self.dbconnector.read(userKey)
            # self.removeEmpty(userData)
        else:
            userData=UserData()
            # self.removeEmpty(userData)
        # print(userData.toString())
        response.addText(userData.toString())
        # self.dbconnector.save(userKey,dicTemp)

    # def emptyResponse(self,dic,key):
    #     dic[key]='kosong'
        # dicTemp={}
        # dicTemp[DataHandler.NO]='kosong'
        # dicTemp[DataHandler.DARI]='kosong'
        # dicTemp[DataHandler.KE]='kosong'
        # dicTemp[DataHandler.HARGA]='kosong'
        # dicTemp[DataHandler.OJEK]='kosong'

    # def removeEmpty(self,dic):
    #     if ~(DataHandler.NO in dic):
    #         self.emptyResponse(dic,DataHandler.NO)
    #     if ~(DataHandler.DARI in dic):
    #         self.emptyResponse(dic,DataHandler.DARI)
    #     if ~(DataHandler.KE in dic):
    #         self.emptyResponse(dic,DataHandler.KE)
    #     if ~(DataHandler.HARGA in dic):
    #         self.emptyResponse(dic,DataHandler.HARGA)
    #     if ~(DataHandler.OJEK in dic):
    #         self.emptyResponse(dic,DataHandler.OJEK)

    # def dicToString(self,dic):
    #     outStr=[]
    #     outStr.append('No:'+self.toStringHandler(dic,DataHandler.NO))
    #     outStr.append('Dari:'+self.toStringHandler(dic,DataHandler.DARI))
    #     outStr.append('Ke:'+self.toStringHandler(dic,DataHandler.KE))
    #     outStr.append('Harga:'+self.toStringHandler(dic,DataHandler.HARGA))
    #     outStr.append('Ojek:'+self.toStringHandler(dic,DataHandler.OJEK))
    #     strOut=""
    #     for s in outStr:
    #         strOut=strOut+s+'\n'
    #     return strOut
    #
    # def toStringHandler(self,dic,key):
    #     if key==DataHandler.DARI:
    #         return dic[DataHandler.DARI]['alamat']
    #     elif key==DataHandler.KE:
    #         return dic[DataHandler.KE]['alamat']
    #     else:
    #         return dic[key]

