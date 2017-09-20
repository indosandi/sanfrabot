class InlineRoute():

    #has dbdriver and dbuser
    def receiveCall(self,bot,chatId,callData):
        #decide entity
        pass

    def routeEntity(self,userEntity,actionEntity):
        if userEntity=='driver':
            self.userToDriver(actionEntity)
        elif userEntity=='passenger':
            self.driverTorUser(actionEntity)

    def userToDriver(self,actionEntity):
        pass

    def driverTorUser(self,actionEntity):
        # send response to user

        # update order data
        pass