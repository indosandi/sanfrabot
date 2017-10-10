# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot.tele as tele

API_TOKEN = '406563676:AAFi4ZDmFr1icgfZg7xXJxXH8x3FawSCgbQ'

bot = telebot.TeleBotMediator(API_TOKEN,'sidewinder.rmq.cloudamqp.com','mwauswng','BZDhlLN18X8YvFYriyJFZWUawYbxYK7c',
                      'mwauswng',5672,True)

bot.polling()
