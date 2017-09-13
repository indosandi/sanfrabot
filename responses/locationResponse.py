from response import Response

class LocationResponse(Response):

    def setUpdateReply(self,bot,message):
        location=message.location
        venue=message.venue
        if location is not None:
            bot.send_location(message.chat.id,location.latitude,location.longitude)
        elif venue is not None:
            address=venue.address
            location=venue.location
            title=venue.title
            bot.send_venue(message.chat.id,location.latitude,location.longitude,title,address)


