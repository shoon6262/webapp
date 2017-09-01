from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')

def index():
	return 'This is the homepage'

@app.route('/LED/<order>')
def profile(order):
	if order == 'ON':
		GPIO.output(8, GPIO.HIGH)
	elif order == 'OFF':
		GPIO.output(8, GPIO.LOW)

	return 'LED %s!!' % order

#start server, default is localhost(127.0.0.1 = localhost = your private ip)
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port = 8888)

