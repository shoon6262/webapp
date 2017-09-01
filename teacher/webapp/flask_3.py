from flask import Flask

app = Flask(__name__) #make instance

@app.route('/') #if you want make '/about', you must make def about()
def index():
	return 'This is the homepage'

@app.route('/profile/<username>')
def profile(username): #username is valiable
	return 'Hey there %s' % username

@app.route('/post/<int:post_id>')
def post(post_id):
	return '<h2>Post ID is %d</h2>' % post_id

#start server, default is localhost(127.0.0.1 = localhost = your private ip)
if __name__ == "__main__":
	app.run(debug = True, host='192.168.0.106', port = 8888)

