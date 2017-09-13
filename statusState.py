import logging

from telegram import (KeyboardButton)
# from telegram.ext import (CommandHandler, Filters, RegexHandler, ConversationHandler, MessageHandler)

from telebot.types import (ReplyKeyboardMarkup, KeyboardButton)
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
        mod['no'] = 'No'
        mod['dari'] = 'Dari'
        mod['ke'] = 'Ke'
        mod['harga'] = 'Harga'
        mod['ojek'] = 'Ojek'
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
        # reply_keyboard = [[KeyboardButton('Kirim no', request_contact=True)]]
        self.respModNo.addReplyKeyboard(markup)
        self.respModNo.addText('Masukan no hp \n No tidak akan dibagikan tanpa izin')
        #
        # self.respModLocation = ButtonResponse()
        # reply_keyboard = [[KeyboardButton('Kirim lokasi', request_location=True)]]
        # self.respModLocation.addText("klik tombol \n ketik /lokasi untuk bantuan")
        # self.respModLocation.addReplyKeyboard(reply_keyboard)
        #
        # keyKirim={}
        # keyKirim['yes']='kirim'
        #
        # self.repsModKe = TextResponse()
        # self.repsModKe.addText('Ketik alamat tujuan\n Ketik /lokasi untuk bantuan')
        # self.repsModKe.addRemoveKeyboard()
        # # reply_keyboard=[[keyKirim['yes']]]
        # # self.repsModKe.addReplyKeyboard(reply_keyboard)
        #
        # self.respHarga=TextResponse()
        # self.respHarga.addText('Ketik harga yang diinginkan \n Kosongkan jika tidak tau harga')
        # self.respHarga.addRemoveKeyboard()
        # # reply_keyboard=[[keyKirim['yes']]]
        # # self.respHarga.addReplyKeyboard(reply_keyboard)
        #
        # self.respOjk=ButtonResponse()
        # self.respOjk.addText('Pilih tipe ojek')
        # tipe={}
        # tipe['motor']='Motor'
        # tipe['mobil']='Mobil'
        # reply_keyboard=[[tipe['motor'],tipe['mobil']]]
        # self.respOjk.addReplyKeyboard(reply_keyboard)
        #
        #
        # replyBool = {}
        # replyBool['y'] = 'yes'
        # replyBool['n'] = 'no'
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
        # self.confLoc = MultiResponse()
        # # confLocTemp=LocationResponse()
        # # self.confLoc.addResponse(confLocTemp)
        # confLocTemp=TextResponse()
        # confLocTemp.addText('Lokasi kamu')
        # self.confLoc.addResponse(confLocTemp)
        # confLocTemp=ButtonResponse()
        # confLocTemp.addText("Apakah lokasi di atas benar")
        # confLocTemp.addReplyKeyboard(reply_keyboard)
        # self.confLoc.addResponse(confLocTemp)
        #
        #
        # self.repsModKeConf = MultiResponse()
        # confLocKeTemp = TextResponse()
        # confLocKeTemp.addText('Lokasi tujuan')
        # self.repsModKeConf.addResponse(confLocKeTemp)
        # confLocKeTemp = ButtonResponse()
        # confLocKeTemp.addText("Apakah lokasi di atas benar")
        # confLocKeTemp.addReplyKeyboard(reply_keyboard)
        # self.repsModKeConf.addResponse(confLocKeTemp)
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
        # handler = PhoneDataHandler()
        # handler.setDbCon(db)
        # self.respModNoSt.setPreDataHandler(handler)
        #
        # self.respModLocationSt = ShareLocationState()
        # self.respModLocationSt.setResponse(self.respModLocation)
        # handler = DariDataHandler()
        # handler.setDbCon(db)
        # self.respModLocationSt.setPreDataHandler(handler)
        #
        # self.repsModKeSt = ShareLocationState()
        # self.repsModKeSt.setResponse(self.repsModKe)
        # handler = KeDataHandler()
        # handler.setDbCon(db)
        # self.repsModKeSt.setPreDataHandler(handler)
        #
        # self.respHargaSt= MessageState()
        # self.respHargaSt.setResponse(self.respHarga)
        # handler= HargaDataHandler()
        # handler.setDbCon(db)
        # self.respHargaSt.setPreDataHandler(handler)
        #
        # self.respOjkSt=OptionButtonState()
        # self.respOjkSt.setResponse(self.respOjk)
        # handler=OjekDataHandler()
        # handler.setDbCon(db)
        # self.respOjkSt.setPreDataHandler(handler)
        #
        # self.confNoSt = OptionButtonState()
        # self.confNoSt.setResponse(self.confNo)
        #
        #
        # self.confLocSt = OptionButtonState()
        # self.confLocSt.setResponse(self.confLoc)
        # handler=ConfLocDataHandler()
        # handler.setDbCon(db)
        # self.confLocSt.setPreDataHandler(handler)
        #
        # self.repsModKeConfSt = OptionButtonState()
        # self.repsModKeConfSt.setResponse(self.repsModKeConf)
        # handler = ConfLocKeDataHandler()
        # handler.setDbCon(db)
        # self.repsModKeConfSt.setPreDataHandler(handler)

        self.router = Router(self.initState)
        handler = RouteHandler()
        handler.setDbCon(db)
        self.router.addHandler(handler)
        # self.router.addRoute(init['find'], self.initState, self.respFJState)
        self.router.addRoute(init['mod'], self.initState, self.modifState)
        # self.router.addRoute(cariJek['selesai'], self.respFJState, self.initState)
        self.router.addRoute(mod['no'], self.modifState, self.respModNoSt)
        # self.router.addRoute(mod['dari'], self.modifState, self.respModLocationSt)
        # self.router.addRoute(mod['ke'], self.modifState, self.repsModKeSt)
        # self.router.addRoute(mod['harga'], self.modifState, self.respHargaSt)
        # self.router.addRoute(mod['ojek'], self.modifState, self.respOjkSt)
        # self.router.addRoute(Router.location, self.repsModKeSt, self.repsModKeConfSt)
        # self.router.addRoute(Router.location, self.respModLocationSt, self.confLocSt)
        self.router.addRoute(self.respModNoSt.name, self.respModNoSt, self.initState)
        # self.router.addRoute(Router.contact, self.respModNoSt, self.initState)
        # # self.router.addRoute(Router.contact, self.respModNoSt, self.confNoSt)
        # self.router.addRoute(replyBool['n'], self.confNoSt, self.respModNoSt)
        # self.router.addRoute(replyBool['y'], self.confNoSt, self.initState)
        # self.router.addRoute(replyBool['n'], self.confLocSt, self.respModLocationSt)
        # self.router.addRoute(replyBool['y'], self.confLocSt, self.initState)
        # self.router.addRoute(replyBool['n'], self.repsModKeConfSt, self.repsModKeSt)
        # self.router.addRoute(replyBool['y'], self.repsModKeConfSt, self.initState)
        # self.router.addRoute(Router.message,self.respHargaSt,self.initState)
        # self.router.addRoute(tipe['motor'],self.respOjkSt,self.initState)
        # self.router.addRoute(tipe['mobil'],self.respOjkSt,self.initState)



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