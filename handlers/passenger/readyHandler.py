from handlers.dataHandler import DataHandler
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import logging
import support.respList as respL
logger = logging.getLogger()

class ReadyHandler(DataHandler):

    def handleData(self, bot,message , response):
        # get driver id
        userKey=self.getUserKey(message)
        listDr,order=self.dbconnector.setReadyOrder(userKey)
        self.sendDriver(bot,message,listDr,order)

    def getUserKey(self,message):
        return str(message.chat.id)

    def sendDriver(self,bot,message,listDr,order):
        if len(listDr)==0:
            chatId=self.getUserKey(message)
            bot.send_message(chatId, respL.noDriver())
        else:
            drivers=listDr[0][::2]
            dists=listDr[0][1::2]
            jmlahDriver=str(len(listDr))
            chatId=self.getUserKey(message)
            bot.send_message(chatId, respL.orderHowMany(jmlahDriver))
            for driver,dist in listDr:
                chatId=driver.split('Driver')[0]
                self.composeResponse(bot,order,dist,chatId)

    def composeResponse(self,bot,order,dist,chatId):
        text=respL.orderToDriver(order.hargaPassenger,dist)
        bot.send_message(chatId,text)
        lat = order.dari['location']['latitude']
        lng = order.dari['location']['longitude']
        address=order.dari['address']
        bot.send_venue(chatId,lat,lng,'Lokasi Penumpang',address)
        lat = order.ke['location']['latitude']
        lng = order.ke['location']['longitude']
        address=order.ke['address']
        bot.send_venue(chatId,lat,lng,'Tujuan Penumpang',address)
        self.composeInline(bot,order,dist,chatId)

    def composeInline(self,bot,order,dist,chatId):
        harga=order.hargaPassenger
        markup=None
        callSetuju=order.id+'@&'+'s'
        callNego=order.id+'@&'+'n'
        if harga =='0':
            #send only one button
            markup = InlineKeyboardMarkup(row_width=2)
            itembtn2 = InlineKeyboardButton('Tetapkan harga', callback_data=callNego)
            markup.add(itembtn2)
        else:
            #send two button
            markup = InlineKeyboardMarkup(row_width=2)
            itembtn1 = InlineKeyboardButton('nego', callback_data=callNego)
            itembtn2 = InlineKeyboardButton('setuju', callback_data=callSetuju)
            markup.add(itembtn1,itembtn2)

        bot.send_message(chatId,respL.hargaInfo(),reply_markup=markup)

