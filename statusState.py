import logging

from telegram import (KeyboardButton)
# from telegram.ext import (CommandHandler, Filters, RegexHandler, ConversationHandler, MessageHandler)

from telebot.types import (ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove)
from dbfunc.dbhash import Dbhash
from handlers.confLocHandler import ConfLocDataHandler
from handlers.confLocKeHandler import ConfLocKeDataHandler
from handlers.dariDataHandler import DariDataHandler
from handlers.hargaDataHandler import HargaDataHandler
from handlers.keDataHandler import KeDataHandler
from handlers.ojekDataHandler import OjekDataHandler
from handlers.phoneDataHandler import PhoneDataHandler
from responses.buttonResponse import ButtonResponse
from responses.initStateHandler import InitStateHandler
from responses.multiResponse import MultiResponse
from responses.phoneNoResponse import PhoneNoResponse
from responses.textResponse import TextResponse
from responses.locationResponse import LocationResponse
from route.router import Router
from states.messageState import MessageState
from states.optionButtonState import OptionButtonState
from states.shareContactState import ShareContactState
from states.shareLocationState import ShareLocationState
from handlers.routeHandler import RouteHandler
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s -%(funcName)10s()- %(levelname)s - %(message)s')

class StatusState(object):
    def __init__(self,  key):
        self.key = key
        self.genAllResponses()

    def genAllResponses(self):
        db=Dbhash()

        init = {}
        init['find'] = 'Cari Ojek'
        init['mod'] = 'Ubah Info'
        init['reset'] = 'Reset'
        markup = ReplyKeyboardMarkup(row_width=1)
        itembtn1 = KeyboardButton(init['find'])
        itembtn2 = KeyboardButton(init['mod'])
        markup.add(itembtn1,itembtn2)
        self.respInit = ButtonResponse()
        reply_keyboard = [[init['find']], [init['mod']]]
        self.respInit.addReplyKeyboard(markup)

        mod = {}
        mod['no'] = 'No hp'
        mod['dari'] = 'Dari'
        mod['ke'] = 'Ke'
        mod['harga'] = 'Harga'
        mod['ojek'] = 'Tipe'
        self.respMod = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=2)
        itembtn1=KeyboardButton(mod['no'])
        itembtn2=KeyboardButton(mod['dari'])
        itembtn3=KeyboardButton(mod['ke'])
        itembtn4=KeyboardButton(mod['harga'])
        itembtn5=KeyboardButton(mod['ojek'])
        markup.add(itembtn1,itembtn2,itembtn3,itembtn4,itembtn5)
        # reply_keyboard = [[mod['no'], mod['dari']],[ mod['ke'], mod['harga']],[ mod['ojek']]]
        self.respMod.addText('Pilih item')
        self.respMod.addReplyKeyboard(markup)

        # cariJek = {}
        # cariJek['selesai'] = 'SELESAI'
        # self.respFJ = ButtonResponse()
        # reply_keyboard = [[cariJek['selesai']]]
        # self.respFJ.addText("Terima kasih")
        # self.respFJ.addReplyKeyboard(reply_keyboard)
        #
        self.respModNo = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=1)
        item=KeyboardButton('Kirim no',request_contact=True)
        markup.add(item)
        self.respModNo.addReplyKeyboard(markup)
        self.respModNo.addText('Masukan no hp \n No tidak akan dibagikan tanpa izin')
        #
        self.respModLocation = ButtonResponse()
        markup=ReplyKeyboardMarkup(row_width=1)
        item=KeyboardButton('Kirim lokasi',request_location=True)
        markup.add(item)
        self.respModLocation.addText("klik tombol \n ketik /lokasi untuk bantuan")
        self.respModLocation.addReplyKeyboard(markup)
        #
        keyKirim={}
        keyKirim['yes']='kirim'
        #
        self.repsModKe = TextResponse()
        self.repsModKe.addText('Ketik alamat tujuan\n Ketik /lokasi untuk bantuan')
        markup=ReplyKeyboardRemove()
        markup.selective=False
        # self.repsModKe.addRemoveKeyboard()
        # # reply_keyboard=[[keyKirim['yes']]]
        self.repsModKe.addReplyMarkup(markup)
        #
        self.respHarga=TextResponse()
        self.respHarga.addText('Ketik harga yang diinginkan \n Keting 0 jika tidak tau harga')
        markup=ReplyKeyboardRemove(selective=False)
        # markup.selective=False
        # self.respHarga.addRemoveKeyboard()
        # # reply_keyboard=[[keyKirim['yes']]]
        self.respHarga.addReplyMarkup(markup)
        #
        self.respOjk=ButtonResponse()
        self.respOjk.addText('Pilih tipe ojek')
        markup=ReplyKeyboardMarkup(row_width=1)
        tipe={}
        tipe['motor']='motor'
        tipe['mobil']='mobil'
        item1=KeyboardButton('motor')
        item2=KeyboardButton('mobil')
        markup.add(item1,item2)
        self.respOjk.addReplyKeyboard(markup)

        # reply_keyboard=[[tipe['motor'],tipe['mobil']]]
        # self.respOjk.addReplyKeyboard(reply_keyboard)
        #
        #
        replyBool = {}
        replyBool['y'] = 'yes'
        replyBool['n'] = 'no'
        markup=ReplyKeyboardMarkup(row_width=2)
        markup.add(replyBool['y'],replyBool['n'])
        reply_keyboard=markup
        # reply_keyboard = [[replyBool['y'], replyBool['n']]]
        #
        # self.confNo = MultiResponse()
        # confNoTemp=PhoneNoResponse()
        # self.confNo.addResponse(confNoTemp)
        # confNoTemp=ButtonResponse()
        # confNoTemp.addText('Apakah no di atas benar')
        # confNoTemp.addReplyKeyboard(reply_keyboard)
        # self.confNo.addResponse(confNoTemp)
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
        #
        self.initState = OptionButtonState()
        self.initState.setResponse(self.respInit)
        self.initState.name='init-state'
        handler=InitStateHandler()
        handler.setDbCon(db)
        self.initState.setPostDataHandler(handler)
        #
        self.modifState = OptionButtonState()
        self.modifState.setResponse(self.respMod)
        self.modifState.name='modif-state'
        #
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
        #
        self.respOjkSt=OptionButtonState()
        self.respOjkSt.setResponse(self.respOjk)
        self.respOjkSt.name='ojek-state'
        handler=OjekDataHandler()
        handler.setDbCon(db)
        self.respOjkSt.setPreDataHandler(handler)
        #
        # self.confNoSt = OptionButtonState()
        # self.confNoSt.setResponse(self.confNo)
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

        self.router = Router(self.initState)
        handler = RouteHandler()
        handler.setDbCon(db)
        self.router.addHandler(handler)
        # self.router.addRoute(init['find'], self.initState, self.respFJState)
        self.router.addRoute(init['mod'], self.initState, self.modifState)
        # self.router.addRoute(cariJek['selesai'], self.respFJState, self.initState)
        self.router.addRoute(mod['no'], self.modifState, self.respModNoSt)
        self.router.addRoute(mod['dari'], self.modifState, self.respModLocationSt)
        self.router.addRoute(mod['ke'], self.modifState, self.repsModKeSt)
        self.router.addRoute(mod['harga'], self.modifState, self.respHargaSt)
        self.router.addRoute(mod['ojek'], self.modifState, self.respOjkSt)
        self.router.addRoute(self.repsModKeSt.name, self.repsModKeSt, self.repsModKeConfSt)
        self.router.addRoute(self.respModLocationSt.name, self.respModLocationSt, self.confLocSt)
        self.router.addRoute(self.respModNoSt.name, self.respModNoSt, self.initState)
        # self.router.addRoute(Router.contact, self.respModNoSt, self.initState)
        # # self.router.addRoute(Router.contact, self.respModNoSt, self.confNoSt)
        # self.router.addRoute(replyBool['n'], self.confNoSt, self.respModNoSt)
        # self.router.addRoute(replyBool['y'], self.confNoSt, self.initState)
        self.router.addRoute(replyBool['n'], self.confLocSt, self.respModLocationSt)
        self.router.addRoute(replyBool['y'], self.confLocSt, self.initState)
        self.router.addRoute(replyBool['n'], self.repsModKeConfSt, self.repsModKeSt)
        self.router.addRoute(replyBool['y'], self.repsModKeConfSt, self.initState)
        self.router.addRoute(self.respHargaSt.name,self.respHargaSt,self.initState)
        self.router.addRoute(tipe['motor'],self.respOjkSt,self.initState)
        self.router.addRoute(tipe['mobil'],self.respOjkSt,self.initState)



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

    # def getConvHandler(self):
    #     conv_handler = ConversationHandler(
    #         entry_points=[RegexHandler('.', self.initState.handler, pass_user_data=True)],
    #         states={
    #             self.router.id: [CommandHandler('reset', self.reset,pass_user_data=True),
    #                              MessageHandler(Filters.location, self.router.route, pass_user_data=True),
    #                              MessageHandler(Filters.contact, self.router.route, pass_user_data=True),
    #                              RegexHandler('.', self.router.route, pass_user_data=True)
    #                              ]},
    #         fallbacks=[CommandHandler('cancel', self.cancel,pass_user_data=True)])
    #     return conv_handler

    def test(self, bot, update):
        print('self test')