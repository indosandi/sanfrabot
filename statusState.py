# -*- coding: UTF-8 -*-
import logging
from dbfunc.dbDriverData import DbDriverData
from dbfunc.dbUserData import DbUserData
from dbfunc.dbredis import DbRedis
from handlers.driver.driverDesc import DriverDesc
from handlers.driver.driverName import DriverName
from handlers.driver.driverNoMotor import DriverNoMotor
from handlers.driver.driverOjek import DriverOjek
from handlers.driver.initDriverHandler import InitDriverHandler
from handlers.driver.driverPhone import DriverPhone
from handlers.passenger.confLocHandler import ConfLocDataHandler
from handlers.passenger.confLocKeHandler import ConfLocKeDataHandler
from handlers.passenger.dariDataHandler import DariDataHandler
from handlers.passenger.hargaDataHandler import HargaDataHandler
from handlers.passenger.initStateHandler import InitStateHandler
from handlers.passenger.keDataHandler import KeDataHandler
from handlers.passenger.ojekDataHandler import OjekDataHandler
from handlers.passenger.phoneDataHandler import PhoneDataHandler
from handlers.routeHandler import RouteHandler
from responses.buttonResponse import ButtonResponse
from responses.locationResponse import LocationResponse
from responses.multiResponse import MultiResponse
from responses.phoneNoResponse import PhoneNoResponse
from responses.textResponse import TextResponse
from route.router import Router
from states.messageState import MessageState
from states.optionButtonState import OptionButtonState
from states.shareContactState import ShareContactState
from states.shareLocationState import ShareLocationState
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove)
from dbfunc.dbOrder import DbOrder
from handlers.driver.outHandler import OutHandler as DOutHandler
from handlers.passenger.outHandler import OutHandler as POutHandler
from handlers.driver.readyHandler import ReadyHandler as DReadyHandler
from handlers.passenger.readyHandler import ReadyHandler as PReadyHandler
from states.locationMessageState import LocationMessageState
from route.inlineRoute import InlineRoute
import support.emojis as emo
from handlers.driver.negoHandler import NegoHandler
from handlers.resetHandler import ResetHandler
import support.respList as respL
from handlers.feedback.appendF import AppendF
from handlers.passenger.lihatHandler import LihatHandler
from handlers.passenger.userName import UserName

# from telegram import (KeyboardButton)
# from telegram.ext import (CommandHandler, Filters, RegexHandler, ConversationHandler, MessageHandler)
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(name)s -%(funcName)10s()- %(levelname)s - %(message)s')
# logger=logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s -%(funcName)10s()- %(levelname)s - %(message)s')
handler = TimedRotatingFileHandler("./log/logWorker.out",when="m",
                                       interval=1440,
                                       backupCount=7)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class StatusState(object):
    """
    Class that define all state and responses
    """
    def __init__(self,  key):
        self.key = key
        self.genAllResponses()

    def genAllResponses(self):
        # db=Dbhash()
        # db=DbRedis()
        db=DbUserData()
        dbDriver=DbDriverData()
        dbOrder=DbOrder()

        initDrPs = {}
        initDrPs['driver'] = 'pengemudi'
        initDrPs['passenger'] = 'penumpang'
        initDrPs['feedback'] = 'feedback'
        markup = ReplyKeyboardMarkup(row_width=2)
        itembtn1 = KeyboardButton(initDrPs['driver'])
        itembtn2 = KeyboardButton(initDrPs['passenger'])
        itembtn3 = KeyboardButton(initDrPs['feedback'])
        markup.add(itembtn1,itembtn2,itembtn3)
        self.respInitDrPs = ButtonResponse()
        self.respInitDrPs.addText(respL.pilihSiapa())
        self.respInitDrPs.addReplyKeyboard(markup)

        # FOR DRIVER MENU --------------------
        initDriver = {}
        initDriver['aktifkan'] = 'Aktifkan Mangkal'
        initDriver['mod'] = 'Ubah Info'
        markup = ReplyKeyboardMarkup(row_width=1)
        itembtn1 = KeyboardButton(initDriver['aktifkan'])
        itembtn2 = KeyboardButton(initDriver['mod'])
        markup.add(itembtn1, itembtn2)
        respInitDriver = ButtonResponse()
        respInitDriver.addReplyKeyboard(markup)

        modD = {}
        modD['no'] = 'No hp'
        # modD['noMotor'] = 'No plat'
        modD['nama'] = 'Nama'
        modD['desc'] = 'Deskripsi'
        modD['ojek'] = 'Kendaraan'
        modDriver= ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=2)
        itembtn1=KeyboardButton(modD['no'])
        # itembtn2=KeyboardButton(modD['noMotor'])
        itembtn3=KeyboardButton(modD['nama'])
        itembtn4=KeyboardButton(modD['desc'])
        itembtn5=KeyboardButton(modD['ojek'])
        markup.add(itembtn1,itembtn3,itembtn4,itembtn5)
        modDriver.addText(respL.ubahInfo())
        modDriver.addReplyKeyboard(markup)


        dvKey={}
        dvKey['checkin']='Perbarui Mangkal'
        dvKey['selese']='Tutup'
        dvResp=ButtonResponse()
        markup = ReplyKeyboardMarkup(row_width=1)
        item1 = KeyboardButton(dvKey['checkin'],request_location=True)
        item2 = KeyboardButton(dvKey['selese'])
        markup.add(item1,item2)
        dvResp.addText(respL.driverMangkal())
        dvResp.addReplyKeyboard(markup)

        noDriver = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=1)
        item=KeyboardButton('Kirim no',request_contact=True)
        markup.add(item)
        noDriver.addReplyKeyboard(markup)
        noDriver.addText(respL.ubahHp())

        namaDriver=TextResponse()
        namaDriver.addText(respL.ubahNama())
        markup=ReplyKeyboardRemove(selective=False)
        namaDriver.addReplyMarkup(markup)

        descMotor=TextResponse()
        descMotor.addText(respL.driverDeskripsi())
        markup=ReplyKeyboardRemove(selective=False)
        descMotor.addReplyMarkup(markup)


        ojkDriver=ButtonResponse()
        ojkDriver.addText(respL.userKendaraan())
        markup=ReplyKeyboardMarkup(row_width=2)
        tipeD={}
        tipeD['motor']='motor'
        tipeD['mobil']='mobil'
        tipeD['bentor']='bentor'
        tipeD['delman']='delman'
        # tipeD['becak']='becak'
        tipeD['kapal']='kapal'
        tipeD['bajaj']='bajaj'
        item1=KeyboardButton('motor')
        item2=KeyboardButton('mobil')
        item3=KeyboardButton('bentor')
        item4=KeyboardButton('delman')
        # item5=KeyboardButton('becak')
        item5=KeyboardButton('kapal')
        item6=KeyboardButton('bajaj')
        markup.add(item1,item2,item3,item4,item5,item6)
        ojkDriver.addReplyKeyboard(markup)

        kembaliDriver = ButtonResponse()
        kembaliDriver.addText(respL.driverGetOrder())
        markup=ReplyKeyboardMarkup(row_width=1)
        typeKembali={}
        typeKembali['kembali']='Kembali'
        item1=KeyboardButton(typeKembali['kembali'])
        markup.add(item1)
        kembaliDriver.addReplyKeyboard(markup)

        feedbackResponse = TextResponse()
        feedbackResponse.addText(respL.feedback())
        markup = ReplyKeyboardRemove(selective=False)
        feedbackResponse.addReplyMarkup(markup)



        initDriverSt = OptionButtonState()
        initDriverSt.setResponse(respInitDriver)
        initDriverSt.name='init-state-driver'
        handler = InitDriverHandler()
        handler.setDbCon(dbDriver)
        initDriverSt.setPostDataHandler(handler)

        dvReadySt= LocationMessageState()
        dvReadySt.name='dvready-state-driver'
        dvReadySt.setResponse(dvResp)
        handler= DReadyHandler()
        handler.setDbCon(dbDriver)
        dvReadySt.setPostDataHandler(handler)
        print(handler,'POST')
        handler= DOutHandler()
        handler.setDbCon(dbDriver)
        dvReadySt.setPreDataHandler(handler)
        print(handler,'PRE')

        modDriverSt = OptionButtonState()
        modDriverSt.setResponse(modDriver)
        modDriverSt.name='mod-state-driver'

        noDriverSt= ShareContactState()
        noDriverSt.setResponse(noDriver)
        noDriverSt.name = 'no-state-driver'
        handler = DriverPhone()
        handler.setDbCon(dbDriver)
        noDriverSt.setPreDataHandler(handler)

        namaDriverSt= MessageState()
        namaDriverSt.setResponse(namaDriver)
        namaDriverSt.name='nama-state-driver'
        handler = DriverName()
        handler.setDbCon(dbDriver)
        namaDriverSt.setPreDataHandler(handler)

        descMotorSt=MessageState()
        descMotorSt.setResponse(descMotor)
        descMotorSt.name='desc-state-driver'
        handler = DriverDesc()
        handler.setDbCon(dbDriver)
        descMotorSt.setPreDataHandler(handler)

        ojkDriverSt=OptionButtonState()
        ojkDriverSt.setResponse(ojkDriver)
        ojkDriverSt.name='ojek-state-driver'
        handler=DriverOjek()
        handler.setDbCon(dbDriver)
        ojkDriverSt.setPreDataHandler(handler)

        kembaliDriverSt = OptionButtonState()
        kembaliDriverSt.setResponse(kembaliDriver)
        kembaliDriverSt.name='kembali-state-driver'

        feedbackResponseSt=MessageState()
        feedbackResponseSt.setResponse(feedbackResponse)
        feedbackResponseSt.name='feedback-state'
        handler=AppendF()
        feedbackResponseSt.setPreDataHandler(handler)
        # END DRIVER MENU --------------------

        init = {}
        init['find'] = 'Cari Ojek'
        init['mod'] = 'Ubah Info'
        markup = ReplyKeyboardMarkup(row_width=1)
        itembtn1 = KeyboardButton(init['find'])
        itembtn2 = KeyboardButton(init['mod'])
        markup.add(itembtn1,itembtn2)
        self.respInit = ButtonResponse()
        reply_keyboard = [[init['find']], [init['mod']]]
        self.respInit.addReplyKeyboard(markup)

        opOrd={}
        opOrd['selese']='Tutup'
        ordStr=ButtonResponse()
        markup = ReplyKeyboardMarkup(row_width=1)
        item = KeyboardButton(opOrd['selese'])
        markup.add(item)
        ordStr.addText(respL.tungguOrder())
        ordStr.addReplyKeyboard(markup)

        mod = {}
        mod['no'] = 'No hp'
        mod['dari'] = 'Dari'
        mod['ke'] = 'Ke'
        mod['harga'] = 'Harga'
        mod['ojek'] = 'Kendaraan'
        mod['nama'] = 'Nama'
        self.respMod = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=2)
        itembtn1=KeyboardButton(mod['no'])
        itembtn2=KeyboardButton(mod['dari'])
        itembtn3=KeyboardButton(mod['ke'])
        itembtn4=KeyboardButton(mod['harga'])
        itembtn5=KeyboardButton(mod['ojek'])
        itembtn6=KeyboardButton(mod['nama'])
        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5,itembtn6)
        self.respMod.addText(respL.ubahInfo())
        self.respMod.addReplyKeyboard(markup)

        self.respModNo = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=1)
        item=KeyboardButton('Kirim no',request_contact=True)
        markup.add(item)
        self.respModNo.addReplyKeyboard(markup)
        self.respModNo.addText(respL.ubahHp())

        self.respModLocation = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=1)
        item=KeyboardButton('Kirim lokasi',request_location=True)
        markup.add(item)

        textDari=respL.lokasiDari()
        self.respModLocation.addText(textDari)
        self.respModLocation.addReplyKeyboard(markup)
        #
        keyKirim={}
        keyKirim['yes']='kirim'
        #
        self.repsModKe = TextResponse()
        # textKe='Beberapa cara mengirim lokasi:\n'
        # textKe+='-> Untuk men-set lokasi baru tekan tombol attachment('+emo.paperclip+') dibawah dan pilih location. Lokasi bisa dipilih ' \
        #             'di map atau di-search\n'
        # textKe+='-> Gunakan foursquare untuk realtime location, ketik "@foursquare alamat-anda", tunggu sampe menu keluar kemudian pilih'
        textKe=respL.lokasiKe()
        self.repsModKe.addText(textKe)
        markup=ReplyKeyboardRemove()
        markup.selective=False
        self.repsModKe.addReplyMarkup(markup)

        namaPassenger = TextResponse()
        namaPassenger.addText(respL.ubahNama())
        markup = ReplyKeyboardRemove(selective=False)
        namaPassenger.addReplyMarkup(markup)
        #
        self.respHarga=TextResponse()
        self.respHarga.addText(respL.userHarga())
        markup=ReplyKeyboardRemove(selective=False)
        self.respHarga.addReplyMarkup(markup)
        #
        self.respOjk=ButtonResponse()
        self.respOjk.addText(respL.userKendaraan())
        markup=ReplyKeyboardMarkup(row_width=2)
        tipe={}
        tipe['motor']='motor'
        tipe['mobil']='mobil'
        tipe['bentor']='bentor'
        tipe['delman']='delman'
        tipe['kapal']='kapal'
        tipe['bajaj']='bajaj'
        item1=KeyboardButton('motor')
        item2=KeyboardButton('mobil')
        item3=KeyboardButton('bentor')
        item4=KeyboardButton('delman')
        item5=KeyboardButton('kapal')
        item6=KeyboardButton('bajaj')
        markup.add(item1,item2,item3,item4,item5,item6)
        self.respOjk.addReplyKeyboard(markup)

        #
        replyBool = {}
        replyBool['y'] = 'yes'
        replyBool['n'] = 'no'
        markup=ReplyKeyboardMarkup(row_width=2)
        markup.add(replyBool['y'],replyBool['n'])
        reply_keyboard=markup
        # reply_keyboard = [[replyBool['y'], replyBool['n']]]
        #
        self.confNo = MultiResponse()
        confNoTemp=PhoneNoResponse()
        self.confNo.addResponse(confNoTemp)
        confNoTemp=ButtonResponse()
        confNoTemp.addText('Apakah no di atas benar')
        confNoTemp.addReplyKeyboard(reply_keyboard)
        self.confNo.addResponse(confNoTemp)
        #
        self.confLoc = MultiResponse()
        confLocTemp=LocationResponse()
        self.confLoc.addResponse(confLocTemp)
        confLocTemp=TextResponse()
        confLocTemp.addText('Lokasi kamu')
        self.confLoc.addResponse(confLocTemp)
        confLocTemp=ButtonResponse()
        confLocTemp.addText("Apakah lokasi di atas benar")
        confLocTemp.addReplyKeyboard(reply_keyboard)
        self.confLoc.addResponse(confLocTemp)
        #
        #
        self.repsModKeConf = MultiResponse()
        confLocKeTemp=LocationResponse()
        self.repsModKeConf.addResponse(confLocKeTemp)
        confLocKeTemp = TextResponse()
        confLocKeTemp.addText('Lokasi tujuan')
        self.repsModKeConf.addResponse(confLocKeTemp)
        confLocKeTemp = ButtonResponse()
        confLocKeTemp.addText("Apakah lokasi di atas benar")
        confLocKeTemp.addReplyKeyboard(reply_keyboard)
        self.repsModKeConf.addResponse(confLocKeTemp)

        kembaliUser = ButtonResponse()
        kembaliUser.addText(respL.userGetOrder())
        typeKembaliUser = {}
        typeKembaliUser['kembali'] = 'Kembali'
        item1 = KeyboardButton(typeKembaliUser['kembali'])
        markup=ReplyKeyboardMarkup(row_width=1)
        markup.add(item1)
        kembaliUser.addReplyKeyboard(markup)

        lihatResponse = ButtonResponse()
        lihatResponse.addText(respL.lihatDriver())
        markup=ReplyKeyboardMarkup(row_width=2)
        typeLihat={}
        typeLihat['lihat']='Lihat'
        typeLihat['order']='Order'
        typeLihat['tutup']='Tutup'
        item1=KeyboardButton(typeLihat['lihat'])
        item2=KeyboardButton(typeLihat['order'])
        item3=KeyboardButton(typeLihat['tutup'])
        markup.add(item1,item2,item3)
        lihatResponse.addReplyKeyboard(markup)
        # STATE----------

        initDrPsSt= OptionButtonState()
        initDrPsSt.setResponse(self.respInitDrPs)
        initDrPsSt.name= 'init-state-drps'

        self.initState = OptionButtonState()
        self.initState.setResponse(self.respInit)
        self.initState.name='init-state'
        handler=InitStateHandler()
        handler.setDbCon(db)
        self.initState.setPostDataHandler(handler)

        passOrderSt = OptionButtonState()
        passOrderSt.setResponse(ordStr)
        handler= PReadyHandler()
        handler.setDbCon(db)
        passOrderSt.setPostDataHandler(handler)
        handler= POutHandler()
        handler.setDbCon(db)
        passOrderSt.setPreDataHandler(handler)

        self.modifState = OptionButtonState()
        self.modifState.setResponse(self.respMod)
        self.modifState.name='modif-state'

        # self.respFJState = OptionButtonState()
        # self.respFJState.setResponse(self.respFJ)
        #
        self.respModNoSt = ShareContactState()
        self.respModNoSt.setResponse(self.respModNo)
        self.respModNoSt.name='phone-state'
        handler = PhoneDataHandler()
        handler.setDbCon(db)
        self.respModNoSt.setPreDataHandler(handler)
        #
        self.respModLocationSt = ShareLocationState()
        self.respModLocationSt.setResponse(self.respModLocation)
        self.respModLocationSt.name='dari-state'
        handler = DariDataHandler()
        handler.setDbCon(db)
        self.respModLocationSt.setPreDataHandler(handler)
        #
        self.repsModKeSt = ShareLocationState()
        self.repsModKeSt.setResponse(self.repsModKe)
        self.repsModKeSt.name='ke-state'
        handler = KeDataHandler()
        handler.setDbCon(db)
        self.repsModKeSt.setPreDataHandler(handler)
        #
        self.respHargaSt= MessageState()
        self.respHargaSt.setResponse(self.respHarga)
        self.respHargaSt.name='harga-state'
        handler= HargaDataHandler()
        handler.setDbCon(db)
        self.respHargaSt.setPreDataHandler(handler)

        namaPassengerSt= MessageState()
        namaPassengerSt.setResponse(namaPassenger)
        namaPassengerSt.name = 'nama-state-user'
        handler = UserName()
        handler.setDbCon(db)
        namaPassengerSt.setPreDataHandler(handler)

        #
        self.respOjkSt=OptionButtonState()
        self.respOjkSt.setResponse(self.respOjk)
        self.respOjkSt.name='ojek-state'
        handler=OjekDataHandler()
        handler.setDbCon(db)
        self.respOjkSt.setPreDataHandler(handler)
        #
        self.confNoSt = OptionButtonState()
        self.confNoSt.setResponse(self.confNo)
        #
        #
        self.confLocSt = OptionButtonState()
        self.confLocSt.setResponse(self.confLoc)
        self.confLocSt.name='conf-dari-state'
        handler=ConfLocDataHandler()
        handler.setDbCon(db)
        self.confLocSt.setPreDataHandler(handler)
        #
        self.repsModKeConfSt = OptionButtonState()
        self.repsModKeConfSt.setResponse(self.repsModKeConf)
        self.repsModKeConfSt.name='conf-ke-state'
        handler = ConfLocKeDataHandler()
        handler.setDbCon(db)
        self.repsModKeConfSt.setPreDataHandler(handler)

        kembaliUserSt = OptionButtonState()
        kembaliUserSt.setResponse(kembaliUser)
        kembaliUserSt.name='kembali-user-state'


        lihatResponseSt=OptionButtonState()
        lihatResponseSt.setResponse(lihatResponse)
        lihatResponseSt.name='lihat-user-state'
        handler=LihatHandler()
        handler.setDbCon(db)
        lihatResponseSt.setPreDataHandler(handler)

        self.router = Router(initDrPsSt)
        # self.router = Router(self.initState)
        dbredis=DbRedis()
        handler = RouteHandler()
        handler.setDbCon(dbredis)
        self.router.addHandler(handler)

        self.inlineRoute=InlineRoute()
        # self.inlineRoute.addBot(self.router.bot)
        self.inlineRoute.addDriverDB(dbDriver)
        self.inlineRoute.addUserDB(db)
        self.inlineRoute.setFinalState('driver',kembaliDriverSt)
        self.inlineRoute.setFinalState('user',kembaliUserSt)
        self.inlineRoute.setRouteHandler(handler)
        # self.inlineRoute.setupRoute()

        handler = NegoHandler()
        handler.setDbCon(dbDriver)
        self.router.addSpecHandler(dvReadySt,handler)
        handler = ResetHandler()
        handler.setDbUser(db)
        handler.setDbCon(dbDriver)
        self.router.setResetHandler(handler)

        self.router.addRoute(initDrPs['driver'],initDrPsSt,initDriverSt)
        self.router.addRoute(initDriver['aktifkan'], initDriverSt, dvReadySt)
        self.router.addRoute(dvKey['selese'],dvReadySt,initDriverSt)
        self.router.addRoute(dvReadySt.name,dvReadySt,dvReadySt)
        self.router.addRoute(initDriver['mod'],initDriverSt,modDriverSt)
        self.router.addRoute(modD['no'],modDriverSt,noDriverSt)
        self.router.addRoute(modD['nama'],modDriverSt,namaDriverSt)
        self.router.addRoute(modD['desc'],modDriverSt,descMotorSt)
        self.router.addRoute(modD['ojek'],modDriverSt,ojkDriverSt)
        self.router.addRoute(noDriverSt.name,noDriverSt,initDriverSt)
        self.router.addRoute(descMotorSt.name,descMotorSt,initDriverSt)
        self.router.addRoute(namaDriverSt.name,namaDriverSt,initDriverSt)
        self.router.addRoute(tipeD['motor'],ojkDriverSt,initDriverSt)
        self.router.addRoute(tipeD['mobil'],ojkDriverSt,initDriverSt)
        self.router.addRoute(tipeD['delman'],ojkDriverSt,initDriverSt)
        self.router.addRoute(tipeD['kapal'],ojkDriverSt,initDriverSt)
        self.router.addRoute(tipeD['bentor'],ojkDriverSt,initDriverSt)
        self.router.addRoute(tipeD['bajaj'],ojkDriverSt,initDriverSt)
        self.router.addRoute(typeKembali['kembali'],kembaliDriverSt,initDriverSt)

        self.router.addRoute(initDrPs['passenger'],initDrPsSt,self.initState)
        self.router.addRoute(init['find'],self.initState,lihatResponseSt)
        self.router.addRoute(typeLihat['order'],lihatResponseSt,passOrderSt)
        self.router.addRoute(typeLihat['lihat'],lihatResponseSt,lihatResponseSt)
        self.router.addRoute(typeLihat['tutup'],lihatResponseSt,self.initState)

        self.router.addRoute(opOrd['selese'],passOrderSt,self.initState)
        self.router.addRoute(init['mod'], self.initState, self.modifState)
        self.router.addRoute(mod['no'], self.modifState, self.respModNoSt)
        self.router.addRoute(mod['dari'], self.modifState, self.respModLocationSt)
        self.router.addRoute(mod['ke'], self.modifState, self.repsModKeSt)
        self.router.addRoute(mod['harga'], self.modifState, self.respHargaSt)
        self.router.addRoute(mod['ojek'], self.modifState, self.respOjkSt)
        self.router.addRoute(mod['nama'], self.modifState, namaPassengerSt)
        self.router.addRoute(self.repsModKeSt.name, self.repsModKeSt, self.repsModKeConfSt)
        self.router.addRoute(self.respModLocationSt.name, self.respModLocationSt, self.confLocSt)
        self.router.addRoute(self.respModNoSt.name, self.respModNoSt, self.initState)
        self.router.addRoute(namaPassengerSt.name, namaPassengerSt, self.initState)
        self.router.addRoute(replyBool['n'], self.confLocSt, self.respModLocationSt)
        self.router.addRoute(replyBool['y'], self.confLocSt, self.initState)
        self.router.addRoute(replyBool['n'], self.repsModKeConfSt, self.repsModKeSt)
        self.router.addRoute(replyBool['y'], self.repsModKeConfSt, self.initState)
        self.router.addRoute(self.respHargaSt.name,self.respHargaSt,self.initState)
        self.router.addRoute(tipe['motor'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['mobil'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['bentor'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['delman'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['kapal'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['bajaj'],self.respOjkSt,self.initState)
        self.router.addRoute(typeKembaliUser['kembali'],kembaliUserSt,self.initState)

        self.router.addRoute(initDrPs['feedback'],initDrPsSt,feedbackResponseSt)
        self.router.addRoute(feedbackResponseSt.name,feedbackResponseSt,initDrPsSt)

    def cancel(self, bot, update, user_data):
        bot.sendMessage(chat_id=update.message.chat_id,text='Ketik /reset untuk ulang')
        return 0

    def reset(self, bot, update,user_data):
        self.router.currentState=self.initState
        self.initState.handlerPostcondition(bot,update,user_data)
        self.initState.handler(bot,update,user_data)
        repText='input salah \n ketik /reset untuk ke awal'
        bot.sendMessage(chat_id=update.message.chat_id,text=repText)
        return 0
