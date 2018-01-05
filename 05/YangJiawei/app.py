#encoding:utf-8
###################################################################################################
__author__ = 'ABigLazyCat'
###################################################################################################
from flask import Flask,request, render_template, redirect
from LogFileAnalyse import LogTopN
import user
import gconf




app = Flask(__name__)



#首页
@app.route('/index/')
def index():
	return render_template('index.html')


#登录
@app.route('/login/', methods = ['GET', 'POST'])
def userlogin():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form.get('username')
		passwd = request.form.get('passwd')	
		if user.userpasswd_vilidate(name, passwd):
			return redirect('/userinfo/%s/'%name)
		else:
			return render_template('login.html', error = u'用户名或密码错误', username = name)




#注册
@app.route('/signup/', methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		name = request.form.get('username')
		passwd = request.form.get('passwd')
		job = request.form.get('job')	
		age = request.form.get('age')
		if user.username_vilidate(name):
			return render_template('signup.html', error = u'用户名已存在')
		elif user.userinfo_vilidate(name, passwd, job, age):
			return render_template('signup.html', error = u'输入不能为空')
		else:
			user.userinfo_add(name, passwd, job, age)
			return redirect('/userinfo/%s/'%name)
	return render_template('signup.html')


#更改，更新
@app.route('/refresh/', methods = ['GET', 'POST'])
def refresh():
	return render_template()






#删除





#查看日志
@app.route('/logfile/top/<n>/')
def topn(n):
	topn = int(n) if str(n).isdigit() else 10
	Top_list = LogTopN(gconf.LOG_FILE, topn)
	return render_template('logfile.html', Top_list = Top_list, Title = 'Top%s'%n)


#查看用户信息
@app.route('/userinfo/<name>/')
def userinfo(name):
	username = name
	passwd, age, job = user.getuserinfo(username)
	print passwd, age, job
	return render_template('userinfo.html', username = username, passwd = passwd, age = age, job = job)






if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8011, debug=True)








