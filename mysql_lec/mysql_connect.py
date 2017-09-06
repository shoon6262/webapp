import MySQLdb

db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
cur = db.cursor()
sql = "insert into mysql_test(id, name, phone) values('shoon6262', 'seonghun', '010-9730-6262')"

try:
	cur.execute(sql)
	db.commit()
except:
	db.rollback()

cur.close()
db.close()
