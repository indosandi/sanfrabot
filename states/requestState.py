from state import State
class RequestState(State):

    def decideNext(self,update,inputDef):
        return True

    def nextCmd(self, message):
        return message.text