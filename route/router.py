import uuid
from telegram.ext.dispatcher import run_async
from states.messageState import MessageState
from states.shareContactState import ShareContactState
from states.shareLocationState import ShareLocationState
import logging
import time
logger = logging.getLogger()
from telebot.tele import TeleBot
# import Exception
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

    def addHandler(self,handler):
        self.handler=handler

    def addBot(self,bot):
        self.bot=bot
        # decor=self.bot.message_handler(commands=['start'],regexp="st",func=None,content_types=['location', 'venue','contact','text'])

        decor=self.bot.message_handler(commands=['start','reset'],func=None)
        # decor=self.bot.message_handler(commands=['start','reset'],func=lambda message: True,content_types=['location','venue','contact'])
        decor(self.routeInit)
        decor=self.bot.message_handler(regexp=".",func=None,content_types=['text'])
        decor(self.route)
        decor=self.bot.message_handler(func=lambda message: True,content_types=['location','venue','contact'])
        decor(self.route)

    def genRandomRef(self):
        Router.contact=uuid.uuid4()
        Router.location=uuid.uuid4()
        Router.message=uuid.uuid4()

    def addRoute(self, nextCmd, currentState, nextState):
        self.nameState[currentState.name] = currentState
        self.inputDef[nextCmd] = currentState
        self.nextDef[(nextCmd, currentState)] = nextState

    def routeInit(self,message):
        self.initState.handlerPostcondition(self.bot,message)
        self.initState.handler(self.bot,message)
        self.currentState=self.initState
        self.handler.setState(message.chat.id,self.initState.name)

    def route(self,message):
        strCurrentState=self.handler.getState(message.chat.id)
        print(strCurrentState,'strCurrentState')
        # word = self.getWordMessage(message)
        if strCurrentState in self.nameState:
            self.currentState=self.nameState[strCurrentState]
        elif strCurrentState is None:
            self.currentState=self.initState
        else:
            logger.error('NO STATE IS POSSIBLE')
        nextCmd = self.getWordMessage(message)
        print(nextCmd)
        if (self.currentState.decideNext(message, self.inputDef)):
            if ((nextCmd, self.currentState) in self.nextDef):
                self.dispatchResponse(message,nextCmd)
            else:
                logger.info("command is not accepted")
                # print(self.nameState)
                # print(self.nextDef)
                # print(nextCmd,self.currentState,'ELSE')
        else:
            repText='input salah \n ketik /reset untuk ke awal'
            # bot.sendMessage(chat_id=update.message.chat_id,text=repText)
            print('here here')

    # @run_async
    def dispatchResponse(self,message,word):
        # fromUser=update.message.from_user
        # chatText=update.message.text
        # if fromUser is not None:
        #     print(fromUser,'fromUser')
        #     if chatText is not None:
        #         print(chatText,'chatText')
        print(message.chat.id,'DISPATCH RESPONSE')
        # time.sleep(5)
        self.currentState.handlerPrecondition(self.bot,message)
        state = self.nextDef[(word, self.currentState)]
        state.handlerPostcondition(self.bot,message)
        state.handler(self.bot, message)
        self.currentState = state
        self.handler.setState(message.chat.id,self.currentState.name)

    def getWordMessage(self, message):
        if isinstance(self.currentState, ShareContactState):
            nextCmd=self.currentState.name
            print('GET SHARECONTACTSTATE')
            # word = Router.contact
        elif isinstance(self.currentState, ShareLocationState):
            nextCmd= self.currentState.name
            print('GET SHARECONTACTSTATE')
            # word = Router.location
        elif isinstance(self.currentState, MessageState):
            nextCmd= self.currentState.name
            # word = Router.message
        else:
            nextCmd = message.text
        return nextCmd

    def routeLocation(self,bot,update):
        print('location here')
        location=update.message.location
        print(location)