import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

LED = 8
TRIGGER = 10
ECHO = 12

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while 1:
        GPIO.output(TRIGGER, False)
        time.sleep(0.5)
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print "Distance: ", distance, "cm"
	
	if distance<10 and GPIO.input(LED)==0:
		os.system("curl http://192.168.0.106:8888/LED/ON")
	elif distance>=10 and GPIO.input(LED)==1:
		os.system("curl http://192.168.0.106:8888/LED/OFF")

except KeyboardInterrupt:
    pass

GPIO.cleanup()
