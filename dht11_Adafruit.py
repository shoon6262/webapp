import datetime
import Adafruit_DHT as dht
import httplib, urllib
import time

KEY = 'EDO0BFH9N0JQNXXI' #API KEY
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept" : "text/plain"}


def dht11_read():
	t_date = datetime.datetime.now()
	current_time = t_date.strftime('%Y-%m-%d %H:%M:%S')
	humidity, temperature = dht.read_retry(dht.DHT11, 14)
	print current_time, ' -> Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temperature, humidity)
	return temperature, humidity

while True:
	temp, hu = dht11_read()
	params = urllib.urlencode({'field1':temp,'field2':hu, 'key':KEY})
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
                conn.request("POST", "/update", params, headers)
                response = conn.getresponse()
                print response.status, response.reason
        except:
                print "Conection failed"
        time.sleep(10)
