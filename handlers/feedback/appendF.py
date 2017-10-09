import logging
import support.append as app
logger = logging.getLogger()
import support.respList as respL
class AppendF(object):

    def handleData(self, bot, message, response):
        userKey = self.getUserKey(message)
        text='{"userKey":'+userKey+','+'"text:""'+message.text+'"}\n'

        try:
            app.append(text)
            logger.info('text is saved to file')
            bot.send_message(userKey,text=respL.feedbackAfter())
        except Exception as e:
            logger.error("fail saving file")

    def getUserKey(self,message):
        return str(message.chat.id)