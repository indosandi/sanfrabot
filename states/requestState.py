from state import State
class RequestState(State):

    def decideNext(self,update,inputDef):
        return True