from response import Response

class TextResponse(Response):

    def setUpdateReply(self,bot,message):
        print(self.replyMarkup,'reply markup')
        bot.send_message(message.chat.id,self.text,reply_markup=self.replyMarkup)
