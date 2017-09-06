import MySQLdb
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
        db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
        cur = db.cursor()
        sql = "select id, name, phone from mysql_test"
        cur.execute(sql)
        rs = cur.fetchall()

        cur.close()
        db.close()
        return render_template('select_id.html', data = rs)


@app.route('/POST/<string:id>/<string:name>/<string:phone>')
def insert(id, name, phone):
        db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
        cur = db.cursor()
        sql = "insert into mysql_test(id, name, phone) values('%s', '%s', '%s')" % (id, name, phone)
        
	try:
		cur.execute(sql)
        	db.commit()

	except:
		db.rollback()
        cur.close()
        db.close()

	#return "<script>document.location.href='/'</script>"        
	return index()


@app.route('/GET/ID/<string:id>')
def get_id(id):
	db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
	cur = db.cursor()
	sql = "select id, name, phone from mysql_test where id='%s'" % id
	cur.execute(sql)
	rs = cur.fetchall()
	
	cur.close()
	db.close()
	return render_template('select_id.html', data = rs)


@app.route('/PUT/<string:id>/<string:name2>/<string:phone2>')
def update(id, name2, phone2):
        db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
        cur = db.cursor()
        sql = "update mysql_test set name='%s', phone='%s' where id='%s'" % (name2, phone2, id)

        try:
                cur.execute(sql)
                db.commit()

        except:
                db.rollback()
        cur.close()
        db.close()

        return index()


@app.route('/DELETE/<string:id>')
def delete(id):
        db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
        cur = db.cursor()
        sql = "delete from mysql_test where id='%s'" % id

        try:
                cur.execute(sql)
                db.commit()

        except:
                db.rollback()
        cur.close()
        db.close()

        return index()


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888)
