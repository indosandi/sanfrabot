from handlers.dataHandler import DataHandler
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import traceback
class NegoHandler(DataHandler):
    def handleData(self, bot,message ):
        driverId = self.getUserKey(message)
        orderId = None
        try:
            query = 'GET ' + driverId + 'nego'
            orderId = self.dbconnector.dbcon.execute_command(query)
        except Exception as e:
            traceback.print_exc()

        if orderId is not None:
            try:
                query = 'DEL ' + driverId + 'nego'
                self.dbconnector.dbcon.execute_command(query)
            except Exception as e:
                traceback.print_exc()

            harga = 'error'
            if message.text is not None:
                harga = str(message.text)
            try:
                # add to set
                query = 'SADD ' + orderId + 'hdriv' + ' ' + driverId
                self.dbconnector.dbcon.execute_command(query)

                # set new harga to driverId
                self.dbconnector.dbcon.set(orderId+'d'+driverId + 'Hrg',harga)
            except Exception as e:
                traceback.print_exc()

            userOrder = orderId.split('Ord')[0]
            # bot.send_message(userOrder, text=driverId + ' ' + harga)
            self.sendDriverAgreeInline(bot,userOrder,driverId,harga,orderId)
        else:
            bot.send_message(driverId, text='input tidak diteruskan')
            # add new price to hargaDriver order set
        pass

    def getUserKey(self,message):
        return str(message.chat.id)+'Driver'

    def sendDriverAgreeInline(self,bot,chatId,driverId,harga,orderId):
                # send only one button
        driver=self.dbconnector.read(driverId)
        nama=driver.nama
        alamat=driver.location['address']
        lat = driver.location['location']['latitude']
        lng = driver.location['location']['longitude']
        response='Driver '+nama+' INGIN harga '+harga+'\n'

        markup = InlineKeyboardMarkup(row_width=1)
        data=orderId+'@&'+'s@&'+driverId+'@&n'
        # if len(data)>70:
        #     data=data[:70]
        #     bot.send_message(driverId, text='Harga terlalu panjang, mungkin dipotong')
        itembtn2 = InlineKeyboardButton('Pilih', callback_data=data)
        markup.add(itembtn2)

        bot.send_message(chatId,response , reply_markup=markup)
        bot.send_venue(chatId,lat,lng,'Lokasi pengemudi',alamat)
