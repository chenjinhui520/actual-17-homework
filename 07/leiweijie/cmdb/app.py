# encoding: utf-8
from flask import Flask, request,render_template,redirect, session, flash
from  log2db import GetTopN
from functools import wraps
import userdb as user

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
    return render_template('public/index_body.html')


@app.route('/logs/',methods=['POST','GET'])
@login_required
def logs():
    if request.method=='GET':
        log_list =  GetTopN()
        return render_template('log_analysis.html',log_list=log_list )
    if request.method=='POST':
        topn = request.form.get('topn')
        # 三目表达式
        topn = int(topn) if str(topn).isdigit() else 10
        title = 'Reboot'
        log_file = request.files.get('files')
        if log_file:
            log_file_name = log_file.filename
            log_file.save(log_file_name)
            GetTopN(log_file=log_file_name, fetch=False)
            log_list =  GetTopN(topN=topn, fetch=True)
            return render_template('log_analysis.html',title=title,log_list=log_list )
        log_list =  GetTopN(topN=topn, fetch=True)
        return render_template('log_analysis.html',title=title,log_list=log_list )


@app.route('/login/',methods=['POST','GET'])
def Login():
    username = request.form.get('username')
    password =  request.form.get('password')
    if request.method == 'GET':
        return render_template('login.html')
    if user.vilidate_login(username,password):
        session['user'] = {'username':username}
        # 跳转到首页
        return redirect('/user/list/')
    else:
        return render_template('login.html',username=username,error=u'用户名或密码错误!')

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
    sex = request.form.get('sex','')
    aihao = request.form.getlist('aihao')
    department = request.form.get('department')
    files = request.files.get('file')
    if files:
        print files.filename
        files.save("/tmp/%s"%files.filename)

    print sex,aihao,department,files



    if request.method == 'GET':
        return render_template('user/user_add.html')
    elif request.method == 'POST':
        _is_ok, error = user.vilidate_find(name,passwd,age,job)
        if _is_ok:
            flash(error)
            return render_template('user/user_add.html')
        else:
            if user.add_user(name,passwd,age,job):
                flash(u'添加: %s成功'%name)
                return redirect('/user/list/')
            else:
                return render_template('user/user_add.html', error=u'用户写入失败.')


@app.route('/user/delete/',methods=['GET'])
@login_required
def user_delete():
    username = request.args.get('username', '')
    uid = request.args.get('uid', '')
    if user.user_delete(uid):
        flash(u'删除: %s成功' % username)
        return redirect('/user/list/')
    else:
        return '用户删除失败.'

@app.route('/user/update/',methods=['POST','GET'])
@login_required
def user_update():
    perams = request.args if request.method == 'GET' else request.form
    uid = perams.get('uid','')
    age = perams.get('age','')
    job = perams.get('job','')
    _user = user.get_user_by_id(uid=uid)[0]
    passwd = perams.get('passwd')
    print uid,age,job,passwd
    if request.method=='GET':
        return render_template("/user/user_update.html",_user=_user)
    if user.user_update(uid=uid, age=age, job=job):
        flash(u'更新：%s成功' % _user['username'])
        return redirect('/user/list/')
    if str(job) ==_user['job'] and int(age) ==_user['age']:
        flash(u'更新：%s成功' % _user['username'])
        return redirect('/user/list/')        
    else:
        flash(u'更新：%s失败' % _user['username'])
        return redirect('/user/list/')

# 用户登出
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')


@app.route('/test/',methods=['GET','POST'])
def test():
    return render_template('test.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

