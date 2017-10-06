from telebot.types import JsonDeserializable
from telebot.types import Venue
from telebot.types import Location
import dbfunc.toJson as toJson

class OrderData(JsonDeserializable):

    USER_SOURCE = 'user_source'
    DARI = 'dari'
    KE = 'ke'
    TIPE = 'tipe'
    HARGA_PASSENGER = 'harga_passenger'
    HARGA_DRIVER = 'harga_driver'
    AGREE_LIST = 'agree_list'
    DRIVER_CHOSEN = 'driver_chosen'
    TIMESTAMP = 'timestamp'
    TIMEFILLED = 'timefilled'
    STATUS = 'status'
    ID = 'id'

    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        userSource = obj[OrderData.USER_SOURCE]
        dari = obj[OrderData.DARI]
        ke = obj[OrderData.KE]
        tipe = obj[OrderData.TIPE]
        hargaPassenger = obj[OrderData.HARGA_PASSENGER]
        hargaDriver = obj[OrderData.HARGA_DRIVER]
        agreeList = obj[OrderData.AGREE_LIST]
        driverChosen = obj[OrderData.DRIVER_CHOSEN]
        timestamp = obj[OrderData.TIMESTAMP]
        timestampFilled = obj[OrderData.TIMEFILLED]
        status = obj[OrderData.STATUS]
        id=obj[OrderData.ID]
        return cls(userSource, dari, ke,tipe, hargaPassenger, hargaDriver, agreeList, driverChosen, timestamp,
                   timestampFilled,status,id)

    def __init__(self,userSource=None,dari=None,ke=None,tipe=None,hargaPassenger=None,hargaDriver=None,agreeList=None,
                 driverChosen=None,timestamp=None,timefilled=None,status=None,id=None):
        self.userSource=userSource
        self.dari=dari
        self.ke=ke
        self.tipe=tipe
        self.hargaPassenger=hargaPassenger
        self.hargaDriver=hargaDriver
        self.agreeList=agreeList
        self.driverChosen=driverChosen
        self.timestamp=timestamp
        self.timefilled=timefilled
        self.status=status
        self.id=id
        self.emptyAll()

    def emptyResponse(self, key):
        if key==OrderData.USER_SOURCE:
            if self.userSource is None:
                self.userSource='0'
        if key==OrderData.DARI:
            if self.dari is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','no address',None)
                self.dari=toJson.toJson(venue)
                # self.dari={'lat':'','long':'','alamat':'kosong'}
        if key==OrderData.KE:
            if self.ke is None:
                location=Location(-6.311525,106.829285)
                venue=Venue(location,'','no address',None)
                self.ke=toJson.toJson(venue)
                # self.ke={'lat':'','long':'','alamat':'kosong'}
        if key== OrderData.HARGA_PASSENGER:
            if self.hargaPassenger is None:
                self.hargaPassenger='0'
        if key==OrderData.HARGA_DRIVER:
            if self.hargaDriver is None:
                self.hargaDriver =''
        if key==OrderData.AGREE_LIST:
            if self.agreeList is None:
                self.agreeList = []
        if key==OrderData.DRIVER_CHOSEN:
            if self.driverChosen is None:
                self.driverChosen =''
        if key==OrderData.TIMESTAMP:
            if self.timestamp is None:
                self.timestamp=0
        if key==OrderData.TIMEFILLED:
            if self.timefilled  is None:
                self.timefilled =0
        if key==OrderData.STATUS:
            if self.status is None:
                self.status=0
        if key==OrderData.TIPE:
            if self.tipe is None:
                self.tipe='motor'
        if key==OrderData.ID:
            if self.id is None:
                self.id=''

    def emptyAll(self):
        self.emptyResponse(OrderData.USER_SOURCE)
        self.emptyResponse(OrderData.DARI)
        self.emptyResponse(OrderData.KE)
        self.emptyResponse(OrderData.HARGA_PASSENGER)
        self.emptyResponse(OrderData.HARGA_DRIVER)
        self.emptyResponse(OrderData.AGREE_LIST)
        self.emptyResponse(OrderData.DRIVER_CHOSEN)
        self.emptyResponse(OrderData.TIMESTAMP)
        self.emptyResponse(OrderData.TIMEFILLED)
        self.emptyResponse(OrderData.STATUS)
        self.emptyResponse(OrderData.TIPE)
        self.emptyResponse(OrderData.ID)

    # def toString(self):
    #     self.emptyAll()
    #     outStr = []
    #     outStr.append('No:' + self.toStringHandler(UserData.NO))
    #     outStr.append('Dari:' + self.toStringHandler(UserData.DARI))
    #     outStr.append('Ke:' + self.toStringHandler(UserData.KE))
    #     outStr.append('Harga:' + self.toStringHandler(UserData.HARGA))
    #     outStr.append('Ojek:' + self.toStringHandler(UserData.OJEK))
    #     strOut = ""
    #     for s in outStr:
    #         strOut = strOut + s + '\n'
    #     strOut=strOut+'Ketik /reset untuk ke awal'
    #     return strOut

    def toDriver(self):
        return ''

    def toPassenger(self):
        return ''

    # def toStringHandler(self, key):
    #     if key == UserData.DARI:
    #         # return self.dari.address
    #         return self.dari['address']
    #     elif key == UserData.KE:
    #         # return self.ke.address
    #         return self.ke['address']
    #     elif key == UserData.NO:
    #         return self.no
    #     elif key == UserData.HARGA:
    #         return self.harga
    #     elif key == UserData.OJEK:
    #         return self.ojek

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
        dic[OrderData.USER_SOURCE] = self.ifNone(self.userSource)
        dic[OrderData.DARI] = self.dari
        dic[OrderData.KE] = self.ke
        dic[OrderData.HARGA_PASSENGER] = self.ifNone(self.hargaPassenger)
        dic[OrderData.HARGA_DRIVER] = self.ifNone(self.hargaDriver)
        dic[OrderData.AGREE_LIST] = self.ifNone(self.agreeList)
        dic[OrderData.DRIVER_CHOSEN] = self.ifNone(self.driverChosen)
        dic[OrderData.TIMESTAMP] = self.ifNone(self.timestamp)
        dic[OrderData.TIMEFILLED] = self.ifNone(self.timefilled)
        dic[OrderData.STATUS] = self.ifNone(self.status)
        dic[OrderData.TIPE] = self.ifNone(self.tipe)
        dic[OrderData.ID] = self.ifNone(self.id)
        return dic

    def ifNone(self,data):
        if data is None:
            return None
        else:
            return data