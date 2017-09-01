from flask import Flask, request

app = Flask(__name__) #make instance

@app.route('/') #if you want make '/about', you must make def about()
def index():
	return 'Method used: %s' % request.method

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
	if request.method == 'POST':
		return 'You are using POST'
	else:
		return 'You are probably using GET'
	


#start server, default is localhost(127.0.0.1 = localhost = your private ip), default port is 5000
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port = 8888)

