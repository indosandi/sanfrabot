# -*- coding: UTF-8 -*-
import logging
import time
from dbfunc.dbUserData import DbUserData
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import support.emojis as emo
import support.respList as respL
import traceback
logger = logging.getLogger()
class InlineRoute(object):
    """ Class that handle inline button event

    Attributes:
        inlineState: the state where inline button is generated
        finalState: the state after order is agreed upon
        routeHandler: handler to get current state from nosql db
        dbConUser: user db connector
        dbConDriver : driver db connector
        bot: bot instace from telebot

    """

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
        """
        The function that handle inline button when pressed.
        :param call: text data that carry from inline button
        :return: None
        """
        data=call.data
        listData=data.split('@&')
        orderId=listData[0]
        buttonId=listData[1]
        pilih='y'
        if len(listData)>2:
            driverId=listData[2]
        if len(listData)>3:
            driverId=listData[2]
            pilih=listData[3]
        else:
            driverId='0'
        userId=str(call.from_user.id)
        userOrder=orderId.split('Ord')[0]
        self.routeEntity(userId,buttonId,orderId,userOrder,driverId,pilih)

    # def proceed(self,bot,nextCmd,state):
    #     # if state is one of a inlineState
    #     if state in self.inlineState:
    #         self.inlineState[state].proceed(bot,nextCmd,state)

    #has dbdriver and dbuser
    # def receiveCall(self,bot,chatId,callData):
    #     #decide entity
    #     pass

    def routeEntity(self,userId,actionEntity,orderId,userOrder,driverId,pilih):
        """
        Function that route to another function depending on text data of inline button
        :param userId: user id
        :param actionEntity: information about which button was pressed
        :param orderId: order Id associated with inline button
        :param userOrder: user Id obtained from order info
        :param driverId: driver id
        :param pilih: 'y'
        :return:
        """
        sender=None
        if str(userId)==str(userOrder):
            sender='Passenger'
        else:
            sender='Driver'

        if actionEntity=='s' and sender=='Driver':
            self.driverAgree(userId,orderId,userOrder)
            # send response driver agree
        elif actionEntity=='s' and sender=='Passenger':
            self.agree(userId,orderId,driverId,pilih)
        elif actionEntity=='n' and sender=='Driver':
            self.driverAskPrice(userId,orderId,userOrder)

    def driverAgree(self,userId,orderId,userOrder):
        """
        Handler when driver press setuju instead of nego
        :param userId: user Id
        :param orderId: order Id
        :param userOrder: user from Order
        :return:
        """

        driverId=str(userId+'Driver')
        orderData=self.dbConUser.readOrder(orderId)
        status=orderData.status
        hargaPas=orderData.hargaPassenger
        harga=hargaPas

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
        """
        Handler to send to penumpang that pengemudi agree
        :param chatId: chat id of telegram
        :param driverId: driver id
        :param harga: harga from order
        :param orderId: order Id
        :return:
        """
                # send only one button
        driver=self.dbConDriver.read(driverId)
        nama=driver.nama
        alamat=driver.location['address']
        lat=driver.location['location']['latitude']
        lng=driver.location['location']['longitude']
        response='Driver '+nama+' SETUJU dengan harga '+harga+'\n'
        markup = InlineKeyboardMarkup(row_width=1)
        data=orderId+'@&'+'s@&'+driverId+'@&s'
        itembtn2 = InlineKeyboardButton('Pilih', callback_data=data)
        markup.add(itembtn2)
        self.bot.send_message(chatId,response , reply_markup=markup)
        self.bot.send_venue(chatId,lat,lng,'Lokasi pengemudi',alamat)

    def driverAskPrice(self,userId,orderId,userOrder):
        """
        Handler when pengemudi press nego button
        :param userId: user Id
        :param orderId: order Id
        :param userOrder: user from Order
        :return:
        """

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
                traceback.print_exc()


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
                    traceback.print_exc()
                self.dbConUser.saveOrder(orderId,orderData)

    def agree(self,userId,orderId,driverId,pilih):
        """
        Handler when penumpang press pilih (memilih driver)
        :param userId: user Id
        :param orderId: order Id
        :param driverId: driver Id
        :param pilih: y
        :return:
        """
        # driverId=str(userId+'Driver')
        orderData = self.dbConUser.readOrder(orderId)
        status=orderData.status
        hargaAkhir='error'
        print(pilih,'PILIH')
        if pilih=='s':
            hargaAkhir=orderData.hargaPassenger
        elif pilih=='n':
            try:
                hargaAkhir=self.dbConUser.dbcon.get(orderId + 'd' + driverId+'Hrg')
            except Exception as e:
                traceback.print_exc()
                hargaAkhir='error'
        else:
            hargaAkhir='error'

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
                text=respL.userSendInfo(passenger.nama,passenger.no,hargaAkhir)
                self.bot.send_message(driverId,text)

                driver=self.dbConDriver.read(driverId)
                text=emo.sirine+emo.sirine+'\n'
                text=respL.driverSendInfo(driver.nama,driver.no,driver.desc,hargaAkhir)
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
