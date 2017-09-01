from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<name>')
def profile(name):
	return render_template('profile.html', key = name)

#start server, default is localhost(127.0.0.1 = localhost = your private ip)
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port = 8888)

