from response import Response
from telegram import ReplyKeyboardRemove

class TextResponse(Response):

    def setUpdateReply(self,bot,message):
        bot.sendMessage(message.chat.id,self.text,reply_markup=self.replyMarkup)
