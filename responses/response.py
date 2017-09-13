class Response(object):
    '''
    Class to define response
    '''

    def __init__(self):
        self.text="Ok"
        self.replyMarkup=None
        self.phone_No=None
        self.location=None
        # self.bot=facb.getBot()

    def addText(self,text):
        self.text=text

    def addReplyMarkup(self,markup):
        self.replyMarkup=markup

    def addReplyKeyboard(self,arrayKeyboard):
        pass

    def setUpdateReply(self,bot,message):
        pass
