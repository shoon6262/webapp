import RPi.GPIO as GPIO
from DHT11_Python.dht11 import DHT11
import httplib, urllib
import time

KEY = 'EDO0BFH9N0JQNXXI' #API KEY
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept" : "text/plain"}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

def dht11_read():
	instance = DHT11(pin = 8)
	result = instance.read()
	if result.is_valid():
		temperature = result.temperature
	else:
		temperature = 0.0
	return temperature	

while True:
	temp = dht11_read()
	params = urllib.urlencode({'field1':temp, 'key':KEY})
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
	except:
		print "Conection failed"
	time.sleep(10)
