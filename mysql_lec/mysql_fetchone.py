import MySQLdb

db = MySQLdb.connect('localhost', 'root', '401gh', 'raspberry')
cur = db.cursor()
sql = "select id, name, phone from mysql_test"

cur.execute(sql)
rs = cur.fetchone()
print rs
print type(rs)

cur.close()
db.close()
