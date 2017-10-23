from telebot.tele import TeleBot
import traceback
from telebot.apihelper import ApiException
import logging
logger = logging.getLogger()
class BotWrap(TeleBot):

    def send_message(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
                     parse_mode=None, disable_notification=None):
        try:
            super(BotWrap,self).send_message(chat_id, text, disable_web_page_preview=disable_web_page_preview,
                                             reply_to_message_id=reply_to_message_id, reply_markup=reply_markup,
                                  parse_mode=parse_mode, disable_notification=disable_notification)
        except ApiException as e:
            logger.error(str(e))

    def send_location(self, chat_id, latitude, longitude, reply_to_message_id=None, reply_markup=None,
                      disable_notification=None):
        try:
            super(BotWrap,self).send_location(chat_id, latitude, longitude, reply_to_message_id=reply_to_message_id
                                              , reply_markup=reply_markup,
                                   disable_notification=disable_notification)
        except ApiException as e:
            logger.error(str(e))

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):
        try:
            super(BotWrap,self).send_contact(chat_id, phone_number, first_name, last_name=last_name,
                                             disable_notification=disable_notification,
                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        except ApiException as e:
            logger.error(str(e))

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, disable_notification=None,
                   reply_to_message_id=None, reply_markup=None):
        try:
            super(BotWrap,self).send_venue(chat_id, latitude, longitude, title, address, foursquare_id=foursquare_id
                                           , disable_notification=disable_notification,
                   reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        except ApiException as e:
            logger.error(str(e))

    def send_photo(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None,
                   disable_notification=None):
        try:
            super(BotWrap,self).send_photo(chat_id, photo, caption=caption, reply_to_message_id=reply_to_message_id
                                           , reply_markup=reply_markup,
                   disable_notification=disable_notification)
        except ApiException as e:
            logger.error(str(e))