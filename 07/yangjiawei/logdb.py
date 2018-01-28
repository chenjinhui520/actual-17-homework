#encoding:utf-8
import MySQLdb as mysql
import gconfdb 


def log_write(file):
	logdict = {}
	loglist = []
	with open(file,'r') as f:
		while True:
			logline = f.readline()
			if not logline:
				break
			else:
				(IP,URL,Status) = (logline.split()[0],logline.split()[6],logline.split()[8])
				logdict[(IP,URL,Status)] = logdict.get((IP,URL,Status),0)+1
		loglist = logdict.items()
		toplist = sorted(loglist, key = lambda x:x[1], reverse = True)
		conn = mysql.connect(host=gconfdb.MYSQL_HOST,port=gconfdb.MYSQL_PORT,user=gconfdb.MYSQL_USER
							,passwd=gconfdb.MYSQL_PASSWD,db=gconfdb.MYSQL_DB,charset=gconfdb.MYSQL_CHARSET)
		cur = conn.cursor()
		for i in toplist:
			args = (i[0][0],i[0][1],i[0][2],i[1])
			sql = "insert into accesslog(ip,url,status,count) values(%s,%s,%s,%s)"
			cur.execute(sql,args)
		conn.commit()
		cur.close()
		conn.close()
		return True , u'文件写入成功'


def log_read(n):
	if n:
		cur = None
		conn = None
		sql = "select * from accesslog limit %s"
		
		try:
			conn = mysql.connect(host=gconfdb.MYSQL_HOST,port=gconfdb.MYSQL_PORT,user=gconfdb.MYSQL_USER
								,passwd=gconfdb.MYSQL_PASSWD,db=gconfdb.MYSQL_DB,charset=gconfdb.MYSQL_CHARSET)
			cur = conn.cursor()
			cur.execute(sql,args=(n,))
			conn.commit()
			rt_db = cur.fetchall()
			return rt_db
		except Exception as e:
			print e
		finally:
			if cur:
				cur.close()
			if conn:
				conn.close()




if __name__ == '__main__':
	log_write(file)
	#print log_read(12)


