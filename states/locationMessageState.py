from state import State
class LocationMessageState(State):

    def decideNext(self,update,inputDef):
        return True

    def nextCmd(self,message):
        #harcoded not good
        if message.venue is not None or message.location is not None or message.text!='Tutup':
            return self.name
        else:
            return message.text