from state import State
class ShareLocationState(State):

    # def modifData(self,update,user_data):
    #     userKey=update.message.chat_id
    #     if (self.readData(userKey) is None):
    #         location=update.message.location
    #         latitude=location.lattitude
    #         longitude=location.longitude

    def decideNext(self,update,inputDef):
        return True