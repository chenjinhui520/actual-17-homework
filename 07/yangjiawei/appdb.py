from flask import Flask ,flash ,redirect ,render_template, request, session
from functools import wraps
import userdb as user
import logdb




app = Flask(__name__)
app.secret_key = '13123dfasdf'

def session_vilidate(func):
	@wraps(func)
	def inner(*args, **kwargs):
		if not session:
			return redirect('/user/login/')
		rt = func(*args, **kwargs)
		return rt
	return inner





@app.route('/index/')
@session_vilidate
def index():
	return render_template('index.html')


@app.route('/user/login/', methods = ['GET','POST'])
def login():
	name = request.form.get('username')
	passwd = request.form.get('password')
	(_isok, tips) = user.login_vilidate(name,passwd)
	if request.method == 'GET':
		return render_template('login.html')
	if _isok:
		flash(tips)
		session['user'] = {'username':name}
		print session
		return redirect('/user/list/')
	else:
		flash(tips)
		return render_template('login.html')


@app.route('/user/list/')
@session_vilidate
def userlist():
	userlist = user.get_users() 
	return render_template('userlist.html',userlist = userlist)


@app.route('/user/signup/', methods = ['GET','POST'])
@session_vilidate
def signup():
	name = request.form.get('username')
	passwd = request.form.get('password')
	age = request.form.get('age')
	job = request.form.get('job')
	(_isok, tips) = user.signup_vilidate(name,passwd,age,job)
	if request.method == 'GET':
		return render_template('signup.html')
	if _isok:
		flash(tips)
		return redirect('/user/list/')
	else:
		flash(tips)
		return render_template('signup.html')

@app.route('/user/update/',methods = ['GET','POST'])
@session_vilidate
def update():
	name = request.args.get('username')
	passwd = request.form.get('password')
	age = request.form.get('age')
	job = request.form.get('job')
	(_isok, tips) = user.update_vilidate(name,passwd,age,job)
	if request.method == 'GET':
		return render_template('update.html',name=name)
	if _isok:
		flash(tips)
		return redirect('/user/list/')
	else:
		flash(tips)
		return render_template('update.html',name=name,passwd=passwd,age=age,job=job)


@app.route('/user/delet/',methods = ['GET','POST'])
@session_vilidate
def delet():
	name = request.args.get('username')
	(_isok, tips) = user.delet_vilidate(name)
	flash(tips)
	return redirect('/user/list/')


@app.route('/user/logout/')
def logout():
	session['user'] = {}
	return redirect('/user/login/')

@app.route('/logs/', methods = ['GET','POST'])
@session_vilidate
def logs():
	n = request.form.get('topn')
	files = request.files.get('files')
	if files:
	    files.save('./logs.txt')
	    log_files = 'logs.txt'
	    _isok,tips = logdb.log_write(log_files)
	    flash(tips)
	    return redirect('/logs/')
	else:
		n = int(n) if str(n).isdigit() else 10
		toplist = logdb.log_read(n)	
		return render_template('logs.html',toplist=toplist)






if __name__ == '__main__':
	app.run(host='127.0.0.1',port=8011,debug=True)
	