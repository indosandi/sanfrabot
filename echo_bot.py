# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot.tele as telebot
import os

API_TOKEN =os.environ['botToken']
rbtHost=os.environ['rbtHost']
rbtUser=os.environ['rbtUser']
rbtVhost=os.environ['rbtVhost']
rbtPort=int(os.environ['rbtPort'])
rbtPass=os.environ['rbtPass']

bot = telebot.TeleBotMediator(API_TOKEN,rbtHost,rbtUser,rbtPass,rbtVhost,rbtPort,True)
                      'mwauswng',5672,True)

bot.polling()
