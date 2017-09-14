from telebot.types import JsonDeserializable
from telebot.types import Venue
from telebot.types import Location
import dbfunc.toJson as toJson

class UserData(JsonDeserializable):

    NO = 'phone_number'
    DARI = 'dari'
    KE = 'ke'
    HARGA = 'harga'
    OJEK = 'ojek'

    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        no = obj['no']
        dari = obj['dari']
        ke = obj['ke']
        harga = obj['harga']
        ojek = obj['ojek']
        return cls(no,dari,ke,harga,ojek)

    def __init__(self,no=None,dari=None,ke=None,harga=None,ojek=None):
        self.no=no
        self.dari=dari
        self.ke=ke
        # self.dari={'lat':None,'long':None,'alamat':None}
        # self.ke={'lat':None,'long':None,'alamat':None}
        self.harga=harga
        self.ojek=ojek
        self.emptyAll()
        print(self.no,'self no')

    def emptyResponse(self, key):
        if key==UserData.NO:
            if self.no is None:
                self.no='kosong'
        if key==UserData.DARI:
            if self.dari is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','kosong',None)
                self.dari=toJson.toJson(venue)
                # self.dari={'lat':'','long':'','alamat':'kosong'}
        if key==UserData.KE:
            if self.ke is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','kosong',None)
                self.ke=toJson.toJson(venue)
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
            # return self.dari.address
            return self.dari['address']
        elif key == UserData.KE:
            # return self.ke.address
            return self.ke['address']
        elif key == UserData.NO:
            return self.no
        elif key == UserData.HARGA:
            return self.harga
        elif key == UserData.OJEK:
            return self.ojek

    def setDari(self,dari):
        print(type(dari))
        if (isinstance(dari,Venue)):
            print('TJOSON')
            self.dari=toJson.toJson(dari)
        else:
            print('NOTJOSON')
            self.dari=dari

    def setKe(self,ke):
        if (isinstance(ke,Venue)):
            self.ke=toJson.toJson(ke)
        else:
            self.ke=ke

    def toJsonUserData(self):
        dic = {}
        dic['no'] = self.ifNone(self.no)
        print(self.dari)
        dic['dari'] = self.dari
        dic['ke'] = self.ke
        dic['harga'] = self.ifNone(self.harga)
        dic['ojek'] = self.ifNone(self.ojek)
        return dic

    def ifNone(self,data):
        # try:
        if data is None:
            return None
        else:
            return data