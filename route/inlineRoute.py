# -*- coding: UTF-8 -*-
import logging
import time
from dbfunc.dbUserData import DbUserData
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import support.emojis as emo
import support.respList as respL
logger = logging.getLogger()
class InlineRoute(object):

    def __init__(self):
        self.inlineState={}
        self.finalState={}

    def setRouteHandler(self,handler):
        self.routeHandler=handler

    def setFinalState(self,key,state):
        self.finalState[key]=state

    def addUserDB(self,db):
        self.dbConUser=db

    def addDriverDB(self,db):
        self.dbConDriver=db

    def addBot(self, bot):
        self.bot = bot

    def addStateInline(self,state,handler):
        self.inlineState[state]=handler

    def setupRoute(self):
        self.bot.callback_query_handler(func=lambda call: True)(self.callback)

    def callback(self,call):
        data=call.data
        listData=data.split('.')
        print(data)
        orderId=listData[0]
        buttonId=listData[1]
        if len(listData)>2:
            driverId=listData[2]
        else:
            driverId='0'
        userId=str(call.from_user.id)
        userOrder=orderId.split('Ord')[0]
        print(orderId,buttonId,userId,userOrder)
        self.routeEntity(userId,buttonId,orderId,userOrder,driverId,call)
        # print(call.data)
        # print(call.chat_instance)
        # print(call.from_user.id)
        # print(call.message)

    def proceed(self,bot,nextCmd,state):
        # if state is one of a inlineState
        if state in self.inlineState:
            self.inlineState[state].proceed(bot,nextCmd,state)

    #has dbdriver and dbuser
    def receiveCall(self,bot,chatId,callData):
        #decide entity
        pass

    def routeEntity(self,userId,actionEntity,orderId,userOrder,driverId,call):
        sender=None
        if str(userId)==str(userOrder):
            sender='Passenger'
        else:
            sender='Driver'

        # user=userEntity.split('Driver')
        # print(user,actionEntity,orderId)
        # if len(user)>1:
        #     sender='Driver'
        #     # self.driverTorUser(actionEntity,orderId)
        # else:
        #     sender='Passenger'
            # self.userToDriver(actionEntity,orderId)
        if actionEntity=='setuju' and sender=='Driver':
            self.driverAgree(userId,orderId,userOrder)
            # send response driver agree
        elif actionEntity=='setuju' and sender=='Passenger':
            self.agree(userId,orderId,driverId,call)
        elif actionEntity=='nego' and sender=='Driver':
            self.driverAskPrice(userId,orderId,userOrder)

    def driverAgree(self,userId,orderId,userOrder):

        driverId=str(userId+'Driver')
        # driverId=str(userId+'Driver')
        orderData=self.dbConUser.readOrder(orderId)
        status=orderData.status
        hargaPas=orderData.hargaPassenger
        harga=hargaPas
        # if driverId in orderData.hargaDriver:
        #     hargaDri=orderData.hargaDriver[driverId]
        #     if orderData.hargaDriver[driverId] != 'x':
        #         harga=hargaDri
        #     else:

        if (status==DbUserData.STATUS_FILLED):
            self.bot.send_message(driverId,'Order sudah diambil')
        elif(status==DbUserData.STATUS_CLOSED):
            self.bot.send_message(driverId,'Order sudah ditutup')
        else:
            agreeList=orderData.agreeList
            if driverId in agreeList:
                agreeList.append(driverId)
                orderData.agreeList = agreeList
                self.bot.send_message(driverId,'Anda sudah setuju')
            else:
                agreeList.append(driverId)
                orderData.agreeList=agreeList
                self.sendDriverAgreeInline(userOrder,driverId,harga,orderId)
                self.dbConUser.saveOrder(orderId,orderData)

    def sendDriverAgreeInline(self,chatId,driverId,harga,orderId):
                # send only one button
        driver=self.dbConDriver.read(driverId)
        nama=driver.nama
        alamat=driver.location['address']
        lat=driver.location['location']['latitude']
        lng=driver.location['location']['longitude']
        response='Driver '+nama+' SETUJU dengan harga '+harga+'\n'
        markup = InlineKeyboardMarkup(row_width=1)
        data=orderId+'.'+'setuju.'+driverId
        itembtn2 = InlineKeyboardButton('Pilih', callback_data=data)
        markup.add(itembtn2)
        self.bot.send_message(chatId,response , reply_markup=markup)
        self.bot.send_venue(chatId,lat,lng,'Lokasi pengemudi',alamat)

    def driverAskPrice(self,userId,orderId,userOrder):

        driverId=str(userId+'Driver')
        orderData=self.dbConUser.readOrder(orderId)
        setHargaDriver=orderData.hargaDriver
        status=orderData.status
        if (status==DbUserData.STATUS_FILLED):
            self.bot.send_message(driverId,'Order sudah diambil')
        elif(status==DbUserData.STATUS_CLOSED):
            self.bot.send_message(driverId,'Order sudah ditutup')
        else:
            res=0
            try:
                query='SISMEMBER '+setHargaDriver+' '+driverId
                res=self.dbConDriver.dbcon.execute_command(query)
            except Exception as e:
                print(str(e))

            print(res,'res')

            if res==1:
                self.bot.send_message(driverId,'Harga sudah dimasukan')
            else:
                self.bot.send_message(driverId,respL.ketikHarga())
                try:
                    query= 'SET '+driverId+'nego '+orderId#' EX 300 NX'
                    self.dbConDriver.dbcon.execute_command(query)
                    query = 'SADD ' + setHargaDriver + ' ' + driverId
                    self.dbConDriver.dbcon.execute_command(query)
                except Exception as e:
                    print(str(e))
                    pass
                self.dbConUser.saveOrder(orderId,orderData)

    def agree(self,userId,orderId,driverId,call):
        # driverId=str(userId+'Driver')
        orderData = self.dbConUser.readOrder(orderId)
        status=orderData.status
        if (status == DbUserData.STATUS_FILLED):
            self.bot.send_message(userId, 'Order sudah diambil')
        elif (status == DbUserData.STATUS_CLOSED):
            self.bot.send_message(userId, 'Order sudah ditutup')
        else:
            orderData.status=DbUserData.STATUS_FILLED
            orderData.timefilled=str(int(time.time()*1000))
            orderData.driverChosen=driverId
            try:
                self.dbConUser.saveOrder(orderId,orderData)
                logger.info('order %s is filled wiht %s',orderId,userId)
                passenger=self.dbConUser.read(userId)
                text=respL.userSendInfo(passenger.nama,passenger.no)
                self.bot.send_message(driverId,text)

                driver=self.dbConDriver.read(driverId)
                text=emo.sirine+emo.sirine+'\n'
                text=respL.driverSendInfo(driver.nama,driver.no,driver.desc)
                self.bot.send_message(userId,text)

                # remove driver from geo
                self.dbConDriver.remove(driverId)
                responseDriver=self.finalState['driver'].response
                responseUser=self.finalState['user'].response
                self.routeHandler.setState(userId,self.finalState['user'].name)
                driverIdState=driverId.split('Driver')[0]
                self.routeHandler.setState(driverIdState,self.finalState['driver'].name)
                self.bot.send_message(userId, responseUser.text, reply_markup=responseUser.replyMarkup)
                self.bot.send_message(driverIdState, responseDriver.text, reply_markup=responseDriver.replyMarkup)

            except Exception as e:
                logger.error(str(e))
