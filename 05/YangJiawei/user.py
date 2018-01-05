#encoding:utf-8
###########################################################
__author__ = 'ABigLazyCat'
###########################################################
import json
import gconf

with open(gconf.USERS_FILE, 'r') as f:
	allusers = json.load(f)
	



#用户名输入验证
def username_vilidate(name):
	if name in allusers:
		return True
	else:
		return False


#用户密码验证
def userpasswd_vilidate(name,passwd):
	for name in allusers:
		if allusers[name]['passwd'] == passwd:
			return True
		else:
			return False



#用户信息输入验证
def userinfo_vilidate(name, passwd, job, age):
	if not passwd or not name or not age or not job:
		return True
	else:
		return False


#用户注册
def userinfo_add(name, passwd, job, age):
	allusers.setdefault(name,{'passwd':passwd,'job':job,'age':age})
	with open(gconf.USERS_FILE, 'w') as f:
		json.dump(allusers,f)
	return True




#提取用户信息
def getuserinfo(username):
	passwd = allusers[username]['passwd']
	age = allusers[username]['age']
	job = allusers[username]['job']
	return passwd, age, job










if __name__ == '__main__':
	name = 'KK'
	passwd = 'KK'
	age = 3
	job = 'Cat'
	#print username_vilidate(name)
	#print userpasswd_vilidate(name, passwd)
	#print getuserinfo('wd')
	print allusers 
	#userinfo_add(name, passwd, age, job)
	#print allusers