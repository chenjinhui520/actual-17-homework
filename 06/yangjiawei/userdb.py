#encoding:utf-8
from gconfdb import logfile
import json
import dbbuild as db
import logdb


def get_users():
	try:
		return db.read_sql()
	except:
		return []

def get_user(username):
	for user in get_users():
		if user[1] == username:
			return user
	return False

def login_vilidate(name,passwd):
	if not name or not passwd:
		return False, u'用户名和密码不能为空'
	if not get_user(name):
		return False, u'用户名不存在'
	else:
		user = get_user(name)
		#print user
		if user[2] == passwd:
			return True, u'用户%s登录成功'%name
		else:
			return False, u'用户名或密码错误'

def signup_vilidate(name,passwd,age,job):
	if not name :
		return False, u'用户名不能为空'
	elif not passwd :
		return False, u'密码不能为空'
	elif not age :
		return False, u'年龄不能为空'
	elif not job :
		return False, u'职位不能为空'
	elif get_user(name):
		return False, u'用户名已存在'
	else:
		if db.write_sql(name,passwd,job,age):
			return True, u'用户%s注册成功'%name
		else:
			return False, u'用户注册失败'

def update_vilidate(name,passwd,age,job):
	users = get_users()
	user = get_user(name)
	new_user =  (name,passwd,age,job)
	if not passwd :
		return False, u'密码不能为空'
	elif not age :
		return False, u'年龄不能为空'
	elif not job :
		return False, u'职位不能为空'
	else:
		if db.modify_sql(name,passwd,job,age):
			return True, u'用户%s更新成功'%name
		else:
			return False, u'用户更新失败'

def delet_vilidate(name):
	db.delet_sql(name)
	return True, u'%s删除成功'%name
		














if __name__ == '__main__':
	#print get_users()
	#print get_user('BB')
	#print signup_vilidate('ORCo','123456',5,'Save')
	#print login_vilidate('Kobe','12456')
	#update_vilidate('jim',123456,26,'Editor')
	#print get_user('jim')
	#print login_vilidate('jim',123456)
	#delet_vilidate('WW')
	#print loglist(10)
	#print get_users()
	#delet_vilidate('Jim')
	update_vilidate('KKK','1234',88,'Kill')
