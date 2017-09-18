from state import State
class OptionButtonState(State):

    def decideNext(self,message,inputDef):
        word=message.text
        if (word in inputDef):
            return True
        else:
            return False

    def nextCmd(self, message):
        return message.text