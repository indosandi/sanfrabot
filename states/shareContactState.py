from state import State
class ShareContactState(State):

    def decideNext(self,message,inputDef):
        if message.contact is not None:
            return True
        else:
            return False
