from handlers.dataHandler import DataHandler
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
class NegoHandler(DataHandler):
    def handleData(self, bot,message ):
        driverId = self.getUserKey(message)
        orderId = None
        try:
            query = 'GET ' + driverId + 'nego '
            orderId = self.dbconnector.dbcon.execute_command(query)
        except Exception as e:
            print(str(e))

        if orderId is not None:
            try:
                query = 'DEL ' + driverId + 'nego '
                self.dbconnector.dbcon.execute_command(query)
            except Exception as e:
                print(str(e))

            harga = ''
            if message.text is not None:
                harga = str(message.text)
            try:
                # add to set
                query = 'SADD ' + orderId + 'hdriv' + ' ' + driverId
                self.dbconnector.dbcon.execute_command(query)

                # set new harga to driverId
                query = 'SET ' + orderId+'d'+driverId + 'Hrg ' + harga
                self.dbconnector.dbcon.execute_command(query)
            except Exception as e:
                print(str(e))

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
        response='Driver '+nama+' INGIN harga '+harga+'\n'
        response=response+'Lokasi :\n'
        response=response+alamat

        markup = InlineKeyboardMarkup(row_width=1)
        data=orderId+'.'+'setuju.'+driverId
        itembtn2 = InlineKeyboardButton('Pilih', callback_data=data)
        markup.add(itembtn2)

        bot.send_message(chatId,response , reply_markup=markup)