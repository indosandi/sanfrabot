from telebot.types import JsonDeserializable
from telebot.types import Venue
from telebot.types import Location
import dbfunc.toJson as toJson

class DriverData(JsonDeserializable):

    NO = 'phone_number'
    # NO_MOTOR= 'no'
    NAMA = 'nama'
    DESC = 'desc'
    OJEK = 'ojek'
    LOKASI = 'location'

    @classmethod
    def de_json(cls, json_string):
        obj = cls.check_json(json_string)
        no = obj[DriverData.NO]
        nama = obj[DriverData.NAMA]
        # noMotor = obj[DriverData.NO_MOTOR]
        desc = obj[DriverData.DESC]
        ojek = obj[DriverData.OJEK]
        location=obj[DriverData.LOKASI]
        return cls(no,nama,desc,ojek,location)
        # return cls(no,nama,noMotor,desc,ojek,location)

    def __init__(self,no=None,nama=None,desc=None,ojek=None,location=None):
    # def __init__(self,no=None,nama=None,noMotor=None,desc=None,ojek=None,location=None):
        self.no=no
        # self.noMotor=noMotor
        self.nama=nama
        self.desc=desc
        self.ojek=ojek
        self.location=location
        self.emptyAll()

    def emptyResponse(self, key):
        if key==DriverData.NO:
            if self.no is None:
                self.no='...'
        # if key== DriverData.NO_MOTOR:
        #     if self.noMotor is None:
        #         self.noMotor='...'
        if key==DriverData.NAMA:
            if self.nama is None:
                self.nama = '...'
        if key==DriverData.DESC:
            if self.desc is None:
                self.desc ='..'
        if key==DriverData.OJEK:
            if self.ojek is None:
                self.ojek='...'
        if key==DriverData.LOKASI:
            if self.location is None:
                location=Location(106.829285,-6.311525)
                venue=Venue(location,'','no address',None)
                self.location=toJson.toJson(venue)

    def emptyAll(self):
        self.emptyResponse(DriverData.NO)
        # self.emptyResponse(DriverData.NO_MOTOR)
        self.emptyResponse(DriverData.NAMA)
        self.emptyResponse(DriverData.DESC)
        self.emptyResponse(DriverData.OJEK)
        self.emptyResponse(DriverData.LOKASI)

    def toString(self):
        self.emptyAll()
        outStr = []
        outStr.append('Nama:' + self.toStringHandler(DriverData.NAMA))
        outStr.append('Phone:' + self.toStringHandler(DriverData.NO))
        # outStr.append('No plat:' + self.toStringHandler(DriverData.NO_MOTOR))
        outStr.append('Tipe:' + self.toStringHandler(DriverData.OJEK))
        outStr.append('Lokasi terakhir:' + self.toStringHandler(DriverData.LOKASI))
        outStr.append('Deskripsi:' + self.toStringHandler(DriverData.DESC))
        strOut = ""
        for s in outStr:
            strOut = strOut + s + '\n'
        strOut=strOut+'Ketik /reset untuk ke awal'
        return strOut

    def setLocation(self,venue):
        if (isinstance(venue,Venue)):
            self.location=toJson.toJson(venue)
        else:
            self.location=venue

    def toStringHandler(self, key):
        if key == DriverData.NO:
            return self.no
        # elif key == DriverData.NO_MOTOR:
        #     return self.noMotor
        elif key == DriverData.NAMA:
            return self.nama
        elif key == DriverData.DESC:
            return self.desc
        elif key == DriverData.OJEK:
            return self.ojek
        elif key == DriverData.LOKASI:
            return self.location['address']

    def toJsonUserData(self):
        dic = {}
        dic[DriverData.NO] = self.ifNone(self.no)
        # dic[DriverData.NO_MOTOR] =self.ifNone(self.noMotor)
        dic[DriverData.NAMA] = self.ifNone(self.nama)
        dic[DriverData.DESC] = self.ifNone(self.desc)
        dic[DriverData.OJEK] = self.ifNone(self.ojek)
        dic[DriverData.LOKASI] = self.ifNone(self.location)
        return dic

    def ifNone(self,data):
        # try:
        if data is None:
            return None
        else:
            return data