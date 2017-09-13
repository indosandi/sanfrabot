from telegram import Location
from telegram import Venue
class UserData(object):

    NO = 'phone_number'
    DARI = 'dari'
    KE = 'ke'
    HARGA = 'harga'
    OJEK = 'ojek'

    def __init__(self):
        self.no=None
        self.dari=None
        self.ke=None
        # self.dari={'lat':None,'long':None,'alamat':None}
        # self.ke={'lat':None,'long':None,'alamat':None}
        self.harga=None
        self.ojek=None
        self.tipe=None

    def emptyResponse(self, key):
        if key==UserData.NO:
            if self.no is None:
                self.no='kosong'
        if key==UserData.DARI:
            if self.dari is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','kosong',None)
                self.dari=venue
                # self.dari={'lat':'','long':'','alamat':'kosong'}
        if key==UserData.KE:
            if self.ke is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','kosong',None)
                self.ke=venue
                # self.ke={'lat':'','long':'','alamat':'kosong'}
        if key== UserData.HARGA:
            if self.harga is None:
                self.harga='kosong'
        if key==UserData.OJEK:
            if self.ojek is None:
                self.ojek='kosong'

    def emptyAll(self):
        self.emptyResponse(UserData.NO)
        self.emptyResponse(UserData.DARI)
        self.emptyResponse(UserData.KE)
        self.emptyResponse(UserData.HARGA)
        self.emptyResponse(UserData.OJEK)

    # def removeEmpty(self, dic):
    #     if ~(DataHandler.NO in dic):
    #         self.emptyResponse(dic, DataHandler.NO)
    #     if ~(DataHandler.DARI in dic):
    #         self.emptyResponse(dic, DataHandler.DARI)
    #     if ~(DataHandler.KE in dic):
    #         self.emptyResponse(dic, DataHandler.KE)
    #     if ~(DataHandler.HARGA in dic):
    #         self.emptyResponse(dic, DataHandler.HARGA)
    #     if ~(DataHandler.OJEK in dic):
    #         self.emptyResponse(dic, DataHandler.OJEK)

    def toString(self):
        self.emptyAll()
        outStr = []
        outStr.append('No:' + self.toStringHandler(UserData.NO))
        outStr.append('Dari:' + self.toStringHandler(UserData.DARI))
        outStr.append('Ke:' + self.toStringHandler(UserData.KE))
        outStr.append('Harga:' + self.toStringHandler(UserData.HARGA))
        outStr.append('Ojek:' + self.toStringHandler(UserData.OJEK))
        strOut = ""
        for s in outStr:
            strOut = strOut + s + '\n'
        return strOut

    def toStringHandler(self, key):
        if key == UserData.DARI:
            return self.dari.address
        elif key == UserData.KE:
            return self.ke.address
        elif key == UserData.NO:
            return self.no
        elif key == UserData.HARGA:
            return self.harga
        elif key == UserData.OJEK:
            return self.ojek
