from flask import Flask

app = Flask(__name__) #make instance

@app.route('/') #if you want make '/about', you must make def about()
def index():
	return 'This is the homepage'

@app.route('/test')
def test():
        return 'test'

@app.route('/tuna')
def tuna():
	return '<h2>Tuna is good</h2>'

#start server, default is localhost(127.0.0.1 = localhost = your private ip)
if __name__ == "__main__":
	app.run(debug = True, host='192.168.0.106', port = 8888)

