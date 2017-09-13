import uuid


class State(object):

    ROUTER_ID=0

    def __init__(self):
        self.id=uuid.uuid4()
        self.name='def'
        self.preDataHandler=None
        self.postDataHandler=None

    def setName(self,name):
        self.name=name

    def setPreDataHandler(self,dh):
        self.preDataHandler=dh;

    def setPostDataHandler(self, dh):
        self.postDataHandler = dh;

    def setResponse(self,response):
        self.response=response

    def handler(self,bot,message):
        self.response.setUpdateReply(bot,message)
        # return State.ROUTER_ID

    def handlerPrecondition(self,bot,message):
        if self.preDataHandler is not None:
            pass
            self.preDataHandler.handleData(bot, message, self.response)

    def handlerPostcondition(self,bot,message):
        if self.postDataHandler is not None:
            pass
            self.postDataHandler.handleData(bot, message, self.response)

    def setName(self,name):
        self.name=name

    def decideNext(self,update,inputDef):
        pass

    # def modifData(self,update,user_data):
    #     pass
        # userKey=update.message.chat_id
        # if (self.readData(userKey) is None):
        #     no_phone=update.message.from_user.contact.phone_number
        #     location=update.message.location
        #     harga=update
        # dic=readData()

    # def writeData(self,key,data):
    #     self.dbcon.save(key,data)
    #
    # def readData(self,key):
    #     return self.dbcon.read(key)



