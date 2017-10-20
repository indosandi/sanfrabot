import os
from telebot.tele import TeleBot


def main():
    # Create the EventHandler and pass it your bot's token.
    botTlgToken=os.environ['botToken']

    # API_TOKEN = '406563676:AAFi4ZDmFr1icgfZg7xXJxXH8x3FawSCgbQ'
    API_TOKEN=os.environ['botToken']
    rbtHost=os.environ['rbtHost']
    rbtUser=os.environ['rbtUser']
    rbtPass=os.environ['rbtPass']
    rbtVhost=os.environ['rbtVhost']
    rbtPort=int(os.environ['rbtPort'])

    # bot = TeleBot(API_TOKEN, 'sidewinder.rmq.cloudamqp.com', 'mwauswng', 'BZDhlLN18X8YvFYriyJFZWUawYbxYK7c',
    #                       'mwauswng', 5672, True)

    bot = TeleBot(API_TOKEN, rbtHost, rbtUser, rbtPass,rbtVhost, rbtPort, True)

    text="Terima kasih sudah memberikan feedback: " \
         "'koordinat maps tidak sesuai saya di surabaya tetapi maps di kebuna... '\n" \
         "Lokasi default memang kebun binatang ragunan, lokasi harus diperbarui terlebih dahulu\n" \
         "Pertanyaan lebih lanjut silahkan chat to @sanfra"
    chatId=""
    bot.send_message(chatId,text)


if __name__ == '__main__':
    main()