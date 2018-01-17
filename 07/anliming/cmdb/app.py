# encoding: utf-8
from flask import Flask, request,render_template,redirect, session, flash
from  Log_Analysis import GetTopN
from functools import wraps
import userdb as user
import logdb
import acc_log
import json
import time
app = Flask(__name__)
app.secret_key = '13123dfasdf'

# 登陆验证装饰器
def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not session:
            return redirect('/login/')
        ret = func(*args, **kwargs)
        return ret
    return inner

@app.route('/')
@login_required
def hello_world():
    title = '51Reboot'
    content={}
    content['H1NAME']='Dashboard'
    content['SMALL']='Index'
    return render_template('public/index.html',contents=content)

@app.route('/logs/',methods=['GET','POST'])
@login_required
def logs():
    if request.method =='GET':
        topn = request.args.get('topn')
        topn = int(topn) if str(topn).isdigit() else 10
        log_list_id=request.args.get('log_list_id')
        log_list = logdb.query_logs(topn,log_list_id)
        return render_template('logs/log_detail.html',log_list=log_list,log_list_id=log_list_id)
    if request.method=='POST':
        topn = request.form.get('topn')
        log_list_id=request.form.get('list_id')
        if topn:
            log_list = logdb.query_logs(int(topn),log_list_id)
        else:
            log_list = logdb.query_logs(10,log_list_id)
        return render_template('logs/log_detail.html',log_list=log_list)

@app.route('/logsdel/')
def logdel():
    logid=request.args.get('log_list_id')
    logdb.del_log(logid)
    topn = request.args.get('topn')
    topn = int(topn) if str(topn).isdigit() else 10
    log_list_id = request.args.get('log_list_id')
    log_list = logdb.query_logs(topn, log_list_id)
    return render_template('logs/log_detail.html',log_list_id=log_list_id)
@app.route('/logs/list/',methods=['GET','POST'])
def loglist():
    log_list = logdb.get_log_list()
    if request.method=='POST':
        log_file = request.files.get('files')
        if log_file:
            file_path='/tmp/'
            save_name = file_path+'%s' % log_file.filename
            log_file.save(save_name)
            logdb.add_log_list(log_file.filename,file_path)
            log_list_id = logdb.get_log_list_id(log_file.filename)
            acc_log.import_log(save_name,log_list_id)
    return render_template('logs/log_list.html',log_list=(log_list))
@app.route('/user/login/',methods=['POST','GET'])
def Login():
    username = request.form.get('username')
    password =  request.form.get('password')
    print username,password
    if request.method == 'GET':
        return render_template('public/login.html')
    if user.vilidate_login(username,password):
        session['user'] = {'username':username}
        # 跳转到首页
        return redirect('/user/list/')
    else:
        return render_template('public/login.html',username=username,error=u'用户名或密码错误!')
@app.route('/user/list/')
@login_required
def UserList():
    all_user = user.get_user()
    return render_template('user/user_list.html',user_list=all_user)
@app.route('/user/add/',methods=['POST','GET'])
@login_required
def UserAdd():
    name = request.form.get('name')
    age = request.form.get('age','')
    passwd = request.form.get('passwd','')
    job = request.form.get('job','')
    if request.method == 'GET':
        return render_template('user/user_add.html')
    elif request.method == 'POST':
        _is_ok, error = user.vilidate_find(name,passwd,age,job)
        if _is_ok:
            flash(error)
            return render_template('/user/user_add.html')
        else:
            if user.add_user(name,passwd,age,job):
                flash(u'添加: %s成功'%name)
                return redirect('/user/list/')
            else:
                return render_template('/user/user_add.html', error=u'用户写入失败.')
@app.route('/user/delete/',methods=['GET'])
@login_required
def user_delete():
    username = request.args.get('username', '')
    if user.user_delete(username):
        flash(u'删除: %s成功_______' % username)
        return redirect('/user/list/')
    else:
        return '用户删除失败.'
@app.route('/user/update/',methods=['POST','GET'])
@login_required
def user_update():
    perams = request.args if request.method == 'GET'else request.form
    uid = perams.get('uid','')
    password = perams.get('password','')
    age = perams.get('age','')
    job = perams.get('job','')
    _user = user.get_user_by_id(uid=uid)[0]
    if request.method == 'GET':
        return render_template('user/user_update.html',_user=_user)
    try:
        user.user_update(password,uid,age,job)
        flash(u'更新: %s成功' %_user['username'])
        return redirect('/user/list/')
    except Exception as e:
        print e
        return '用户更新失败.'
# 用户登出
@app.route('/user/logout/')
def logout():
    session.pop('username', None)
    return redirect('/user/login/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

