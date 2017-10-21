import os


from statusState import StatusState
from telebot.tele import TeleBot


def main():
    # Create the EventHandler and pass it your bot's token.
    botTlgToken=os.environ['botToken']

    API_TOKEN=os.environ['botToken']
    rbtHost=os.environ['rbtHost']
    rbtUser=os.environ['rbtUser']
    rbtPass=os.environ['rbtPass']
    rbtVhost=os.environ['rbtVhost']
    rbtPort=int(os.environ['rbtPort'])

    bot = TeleBot(API_TOKEN, rbtHost, rbtUser, rbtPass,rbtVhost, rbtPort, True)
    sts=StatusState(None)
    sts.router.addBot(bot)
    sts.inlineRoute.addBot(bot)
    sts.inlineRoute.setupRoute()
    sts.router.bot.polling()


if __name__ == '__main__':
    main()
