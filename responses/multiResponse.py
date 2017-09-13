from response import Response
class MultiResponse(Response):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.listResponse=[]

    def addResponse(self,response):
        self.listResponse.append(response)

    def setUpdateReply(self,bot,message):
        for response in self.listResponse:
            response.setUpdateReply(bot,message)