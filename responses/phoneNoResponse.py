from response import Response

class PhoneNoResponse(Response):

    def setUpdateReply(self,bot,message):
        phone_number=message.contact.phone_number
        first_name=message.contact.first_name
        last_name=message.contact.last_name
        bot.send_contact(chat_id=message.chat.id,phone_number=phone_number,first_name=first_name
                         ,last_name=last_name,reply_markup=None)
