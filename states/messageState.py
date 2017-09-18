from state import State
class MessageState(State):

    def decideNext(self,update,inputDef):
        return True

    def nextCmd(self, message):
        return self.name
