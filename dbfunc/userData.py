from telebot.types import JsonDeserializable
from telebot.types import Venue
from telebot.types import Location
import dbfunc.toJson as toJson

class UserData(JsonDeserializable):

    NO = 'no'
    NAMA = 'nama'
    DARI = 'dari'
    KE = 'ke'
    HARGA = 'harga'
    OJEK = 'ojek'

    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        print(obj)
        no = obj['no']
        dari = obj['dari']
        ke = obj['ke']
        harga = obj['harga']
        ojek = obj['ojek']
        nama =obj['nama']
        return cls(no=no,dari=dari,ke=ke,harga=harga,ojek=ojek,nama=nama)

    def __init__(self,no=None,dari=None,ke=None,harga=None,ojek=None,nama=None,msg=None):
        self.no=no
        self.nama=nama
        self.dari=dari
        self.ke=ke
        # self.dari={'lat':None,'long':None,'alamat':None}
        # self.ke={'lat':None,'long':None,'alamat':None}
        self.harga=harga
        self.ojek=ojek
        self.getNo(msg)
        self.emptyAll()

    def getNo(self,msg):
        if msg is not None:
            if (msg.chat.first_name is not None):
                self.nama=msg.chat.first_name

    def emptyResponse(self, key):
        if key==UserData.NO:
            if self.no is None:
                self.no='...'
        if key==UserData.DARI:
            if self.dari is None:
                location=Location(106.829285,-6.311525)
                venue=Venue(location,'','no address',None)
                self.dari=toJson.toJson(venue)
                # self.dari={'lat':'','long':'','alamat':'kosong'}
        if key==UserData.KE:
            if self.ke is None:
                location=Location(106.829285,-6.311525)
                venue=Venue(location,'','no address',None)
                self.ke=toJson.toJson(venue)
                # self.ke={'lat':'','long':'','alamat':'kosong'}
        if key== UserData.HARGA:
            if self.harga is None:
                self.harga='...'
        if key==UserData.OJEK:
            if self.ojek is None:
                self.ojek='motor'
        if key == UserData.NAMA:
            if self.nama is None:
                self.nama = '.'

    def emptyAll(self):
        self.emptyResponse(UserData.NO)
        self.emptyResponse(UserData.DARI)
        self.emptyResponse(UserData.KE)
        self.emptyResponse(UserData.HARGA)
        self.emptyResponse(UserData.OJEK)
        self.emptyResponse(UserData.NAMA)

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
        outStr.append('Nama:' + self.toStringHandler(UserData.NAMA))
        outStr.append('Dari:' + self.toStringHandler(UserData.DARI))
        outStr.append('Ke:' + self.toStringHandler(UserData.KE))
        outStr.append('Harga:' + self.toStringHandler(UserData.HARGA))
        outStr.append('Ojek:' + self.toStringHandler(UserData.OJEK))
        strOut = ""
        for s in outStr:
            strOut = strOut + s + '\n'
        strOut=strOut+'Ketik /reset untuk ke awal'
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
        elif key == UserData.NAMA:
            return self.nama

    def setDari(self,dari):
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
        dic[UserData.NO] = self.ifNone(self.no)
        dic[UserData.DARI] = self.dari
        dic[UserData.KE] = self.ke
        dic[UserData.HARGA] = self.ifNone(self.harga)
        dic[UserData.OJEK] = self.ifNone(self.ojek)
        dic[UserData.NAMA] = self.ifNone(self.nama)
        return dic

    def ifNone(self,data):
        # try:
        if data is None:
            return None
        else:
            return data