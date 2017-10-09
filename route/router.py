import uuid
import logging
import support.respList as respL
logger = logging.getLogger()
class Router(object):
    contact = 'contact1235'
    location = 'location1235'
    message = 'message1235'

    def __init__(self, state):
        self.inputDef = {}
        self.nextDef = {}
        self.currentState = state
        self.initState=state
        self.id = 0
        self.bot=None
        self.nameState={}
        self.specHandler={}

    def addHandler(self,handler):
        self.handler=handler

    def setResetHandler(self,handler):
        self.resetHandler=handler

    def addBot(self,bot):
        self.bot=bot

        decor=self.bot.message_handler(commands=['start','reset'],func=None)
        decor(self.routeInit)
        decor=self.bot.message_handler(commands=['lokasi'],func=None)
        decor(self.lokasiHandler)
        decor=self.bot.message_handler(regexp=".",func=None,content_types=['text'])
        decor(self.route)
        decor=self.bot.message_handler(func=lambda message: True,content_types=['location','venue','contact'])
        decor(self.route)

    def addSpecHandler(self,key,handler):
        self.specHandler[key]=handler

    def genRandomRef(self):
        Router.contact=uuid.uuid4()
        Router.location=uuid.uuid4()
        Router.message=uuid.uuid4()

    def addRoute(self, nextCmd, currentState, nextState):
        self.nameState[currentState.name] = currentState
        self.inputDef[nextCmd] = currentState
        self.nextDef[(nextCmd, currentState)] = nextState

    def lokasiHandler(self,message):
        if (self.currentState.name=='dari-state'):
            self.bot.send_message(message.chat.id,respL.lokasiDariLengkap())
        elif (self.currentState.name=='ke-state'):
            self.bot.send_message(message.chat.id,respL.lokasiKeLengkap())

    def lokasiKeHandler(self,message):
        self.bot.send_message(message.chat.id,respL.lokasiKeLengkap())

    def routeInit(self,message):
        self.initState.handlerPostcondition(self.bot,message)
        self.initState.handler(self.bot,message)
        self.currentState=self.initState
        self.resetHandler.handleData(self.bot,message,None)
        self.handler.setState(message.chat.id,self.initState.name)

    def route(self,message):

        strCurrentState=self.handler.getState(message.chat.id)
        print(strCurrentState,'strCurrentState',message.chat.id)
        if strCurrentState in self.nameState:
            self.currentState=self.nameState[strCurrentState]
        elif strCurrentState is None:
            self.currentState=self.initState
        else:
            logger.error('NO STATE IS POSSIBLE')
        nextCmd = self.getWordMessage(message)
        if (self.currentState.decideNext(message, self.inputDef)):
            if ((nextCmd, self.currentState) in self.nextDef):
                print('DISPATCH RESPONSE')
                self.dispatchResponse(message,nextCmd)
            else:
                logger.info("command is not accepted")
                self.handleSpec(self.currentState,self.bot,message)
        else:
            repText=respL.inputSalah()
            self.bot.send_message(chat_id=message.chat.id,text=repText)
            print('here here')

    def dispatchResponse(self,message,word):

        self.currentState.handlerPrecondition(self.bot,message)
        state = self.nextDef[(word, self.currentState)]
        state.handlerPostcondition(self.bot,message)
        state.handler(self.bot, message)
        self.currentState = state
        self.handler.setState(message.chat.id,self.currentState.name)

    def getWordMessage(self, message):
        return self.currentState.nextCmd(message)

    def handleSpec(self,state,bot,message):
        if state in self.specHandler:
            self.specHandler[state].handleData(bot,message)