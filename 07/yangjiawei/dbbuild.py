import MySQLdb as mysql
import gconfdb



def sql_run(sql,args):
	cur = None
	conn = None
	try:
		conn = mysql.connect(host=gconfdb.MYSQL_HOST,port=gconfdb.MYSQL_PORT,user=gconfdb.MYSQL_USER
							,passwd=gconfdb.MYSQL_PASSWD,db=gconfdb.MYSQL_DB,charset=gconfdb.MYSQL_CHARSET)
		cur = conn.cursor()
		cur.execute(sql,args)
		conn.commit()
	except Exception as e:
		print e
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()

def read_sql():
	sql = 'select * from user'
	cur = None
	conn = None
	try:
		conn = mysql.connect(host=gconfdb.MYSQL_HOST,port=gconfdb.MYSQL_PORT,user=gconfdb.MYSQL_USER
							,passwd=gconfdb.MYSQL_PASSWD,db=gconfdb.MYSQL_DB,charset=gconfdb.MYSQL_CHARSET)
		cur = conn.cursor()
		conn.commit()
		cur.execute(sql)
		rt_db = cur.fetchall()
		return rt_db
	except Expection as e:
		print e
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()
	
def write_sql(name,passwd,job,age):
	sql = "insert into user(username,password,job,age) values(%s,%s,%s,%s)"
	args = (name,passwd,job,age)
	sql_run(sql,args)
	return True

def modify_sql(name,passwd,job,age):
	sql = "update user set password=%s,job=%s,age=%s where username=%s"
	args = (passwd,job,age,name)
	sql_run(sql,args)
	return True

def delet_sql(name):
	sql = "delete from user where username='%s'"%name
	args = None
	sql_run(sql,args)
	return True






if __name__ == '__main__':
	print read_sql()
	#write_sql('SSA','123456','ASSS',1)
	#modify_sql('BB','123456','Baby',13)
	delet_sql('%s')


