from handlers.dataHandler import DataHandler
import logging
import support.respList as respL
import support.staticmap as gmap
import traceback
logger = logging.getLogger()

class LihatHandler(DataHandler):

    def handleData(self, bot,message , response):
        # hardcoded
        if message.text=='Order' or message.text=='Tutup':
            return
        userKey=self.getUserKey(message)
        lat,lng,tipe=self.getInfo(userKey)
        if (lat is None or lng is None or tipe is None):
            bot.send_message(userKey,text=respL.errorServ())
        else:
            listDr=self.getRadius(tipe,lng,lat)
            if len(listDr) == 0:
                chatId = self.getUserKey(message)
                bot.send_message(chatId, respL.noDriver())
            else:
                drivers = listDr[0][::2]
                dists = listDr[0][1::2]
                jmlahDriver = str(len(listDr))
                marker=[]
                for driver, dist in listDr:
                    chatId = driver.split('Driver')[0]
                    [[lngD,latD]]=self.getPos(driver,tipe)
                    marker.append({"lat":latD,"lng":lngD})
                url=gmap.genUrl({"lat":lat,"lng":lng},marker)
                try:
                    bot.send_photo(userKey,url)
                    bot.send_message(userKey,text=respL.lihatDriverImg(jmlahDriver))
                except Exception as e:
                    bot.send_message(userKey,text=respL.errorServ())
                    logger.info("service error")

    def getUserKey(self,message):
        return str(message.chat.id)

    def getInfo(self,chatId):
        try:
            userData=self.dbconnector.read(chatId)
            lat=userData.dari['location']['latitude']
            lng=userData.dari['location']['longitude']
            tipe=userData.ojek
            return lat,lng,tipe
        except Exception as e:
            traceback.print_exc()
            return None,None,None

    def getRadius(self,tipe,lng,lat):

        query='GEORADIUS '+str(tipe)+' '+str(lng)+' '+str(lat)+' '+'2 km WITHDIST ASC'
        out=None
        try:
            out=self.dbconnector.dbcon.execute_command(query)
        except Exception as e:
            logger.error("fail get radius")
            logger.error(str(e))
        if out is None:
            return []
        else:
            return out

    def sendDriver(self,bot,message,listDr,order):
        if len(listDr)==0:
            chatId=self.getUserKey(message)
            bot.send_message(chatId, respL.noDriver())
        # if len(listDr)>0:
        else:
            drivers=listDr[0][::2]
            dists=listDr[0][1::2]
            jmlahDriver=str(len(listDr))
            for driver,dist in listDr:
                chatId=driver.split('Driver')[0]
                self.composeResponse(bot,order,dist,chatId)


    def getPos(self,driverId,tipe):
        query='GEOPOS '+tipe+' '+driverId
        out=None
        try:
            out=self.dbconnector.dbcon.execute_command(query)
        except Exception as e:
            logger.error("fail get driver pos")
            logger.error(str(e))
        if out is None:
            return []
        else:
            return out
