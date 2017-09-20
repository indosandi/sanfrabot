from handlers.dataHandler import DataHandler
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import logging
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
        print(listDr,'LIST DIR')
        if len(listDr)>0:
            drivers=listDr[0][::2]
            dist=listDr[0][1::2]
            for driver,dist in zip(drivers,dist):
                chatId=driver.split('Driver')[0]
                self.composeResponse(bot,order,dist,chatId)

    def composeResponse(self,bot,order,dist,chatId):
        text='ORDER!!!!!\n'
        text=text+'DARI: '+order.dari['address']+'\n'
        text=text+'KE: '+order.ke['address']+'\n'
        text=text+'HARGA: '+order.hargaPassenger+'\n'
        text=text+'jarak ke penumpang '+dist+' KM\n'
        bot.send_message(chatId,text)
        lat = order.dari['location']['latitude']
        lng = order.dari['location']['longitude']
        bot.send_venue(chatId,lat,lng,'Lokasi Penumpang','')
        self.composeInline(bot,order,dist,chatId)

    def composeInline(self,bot,order,dist,chatId):
        harga=order.hargaPassenger
        markup=None
        callSetuju=order.id+'.'+'setuju'
        callNego=order.id+'.'+'nego'
        if harga =='0':
            #send only one button
            markup = InlineKeyboardMarkup(row_width=2)
            itembtn2 = InlineKeyboardButton('setuju', callback_data=callSetuju)
            markup.add(itembtn2)
        else:
            #send two button
            markup = InlineKeyboardMarkup(row_width=2)
            itembtn1 = InlineKeyboardButton('nego', callback_data=callNego)
            itembtn2 = InlineKeyboardButton('setuju', callback_data=callSetuju)
            markup.add(itembtn1,itembtn2)

        bot.send_message(chatId,'Pilih',reply_markup=markup)

    def receiveCall(self,callData):
        print(callData)
        #decide entity
        pass

    def routeEntity(self,userEntity,actionEntity):
        if userEntity=='driver':
            self.userToDriver(actionEntity)
        elif userEntity=='passenger':
            self.driverTorUser(actionEntity)

    def userToDriver(self,actionEntity):
        pass

    def driverTorUser(self,actionEntity):
        # send response to user

        # update order data
        pass
