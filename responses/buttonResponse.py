from response import Response

class ButtonResponse(Response):
    def addReplyKeyboard(self,markup ):
        self.replyMarkup = markup

    def setUpdateReply(self,bot,message):
        bot.send_message(message.chat.id,self.text, reply_markup=self.replyMarkup)

