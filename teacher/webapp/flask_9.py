from flask import Flask, render_template
from dict import Articles
# from file = module import class or method
# if you want search module in folder, you can write like follow line.. 
# from folder.data import Articles

app = Flask(__name__)

Articles = Articles() # make instance

@app.route('/')
def index():
	return 'hi dictionary'

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

@app.route('/article/<int:id>')
def article(id):
	return render_template('article.html', id = id, articles = Articles)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8888)
