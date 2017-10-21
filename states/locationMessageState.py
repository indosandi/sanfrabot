from state import State
class LocationMessageState(State):

    def decideNext(self,update,inputDef):
        return True

    def nextCmd(self,message):
        #harcoded not good
        if message.location is not None:
            return self.name
        else:
            return message.text