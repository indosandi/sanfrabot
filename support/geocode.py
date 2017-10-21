import googlemaps
import os
import logging


logger = logging.getLogger()
apiKey=os.environ['GMAP']
gmaps = googlemaps.Client(key=apiKey,timeout=15)
errorLat=-6.16745433018
errorLng=106.821003383
def getLatLng(address):

    try:
        geocode_result = gmaps.geocode(address)
        return geocode_result[0]['geometry']['location']
    except Exception as e:
        logger.error('geocode error')
        logger.info(str(e))
        return {u'lat':errorLat,u'lng':errorLng}

def getAddress(lat,lng):
    try:
        reverse_geocode_result = gmaps.reverse_geocode((lat,lng))
        return reverse_geocode_result[0]['formatted_address']
    except Exception as e:
        logger.error('reverse gecode error')
        logger.info(str(e))
        return 'error ketika mendapatkan alamat'
