# -*- coding:utf8 -*-
from flask import Flask, request, render_template, \
    redirect, flash, url_for, session

from db_utlis import *
from check_utils import *
from functools import wraps
from handle_logs import execute_manysql, handle_logs, fetch_result
import json

app = Flask(__name__)
# 使用flash必须要有这条语句，没有会报
app.secret_key = 'some_secret'

# 登陆验证装饰器
def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not session:
            flash('Please login!')
            return redirect('/login/')
        ret = func(*args, **kwargs)
        return ret
    return inner


# 用户登录
@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        users = fetch_users()
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        try:
            # 用户名和密码验证
            CheckLogin(username, password)
        except Exception as err:
            flash(str(err))
            return redirect(url_for('login'))
        else:
            # 登陆成功跳转
            session['user'] = {'username': username}
            return redirect(url_for('user'))

# 用户注册
@app.route('/user/add/', methods=['GET', 'POST'])
def user_add():
    if request.method == 'GET':
        return render_template('user/user_add.html')

    if request.method == 'POST':
        users = fetch_users()

        newuser = request.form.get('username', None)
        password = request.form.get('password', None)
        retype_password = request.form.get('retype_password', None)
        age = request.form.get('age',None)
        job = request.form.get('job', None)
        print newuser, password, retype_password, age, job

        try:

            # 密码长度检测
            CheckPasswordLen(password)
            # 二次验证密码
            DoubleCheckPassword(password, retype_password)
            # 用户名是否已注册
            UsernameAlreadyExist(newuser, users)
            # 用户信息禁止为空
            CheckInputIsEmpty(newuser, age, job)
        except Exception as err:
            return json.dumps({'is_ok': False, 'error': str(err)})
        else:
            add_user(newuser, password, age, job)
            return json.dumps({'is_ok': True, 'error': ''})

# 用户页面
@app.route('/user/')
@login_required
def user():
    flash('Welcome back {}!'.format(session['user']['username']))

    # 需要获取全部用户数据
    user_dict = fetch_all_information()

    return render_template('user/user.html', user_dict=user_dict)



# 新的密码更新
@app.route('/user/change-passwd/', methods=['POST'])
@login_required
def change_passwd():
    update_name = request.form.get('update_name')
    admin = session['user']['username']
    admin_passwd = request.form.get('admin_passwd')
    new_passwd = request.form.get('new_passwd')
    retype_passwd = request.form.get('retype_passwd')

    try:
        CheckLogin(admin, admin_passwd)
        CheckPasswordLen(new_passwd)
        DoubleCheckPassword(new_passwd, retype_passwd)
    except Exception as err:

        return json.dumps({'is_ok': False, 'error': str(err)})
    else:
        change_password(update_name, new_passwd)
        return json.dumps({'is_ok': True, 'error': ''})



@app.route('/user/update/<username>/', methods=['GET', 'POST'])
@login_required
def update(username):
    user_dict = fetch_information(username)

    if request.method == 'GET':
        return render_template('user/user_update.html', username=username, user_dict=user_dict)


    if request.method == 'POST':
        # admin对用户数据进行修改的代码和注册是一样的，怎么优化？

        user_dict = fetch_information(username)

        age = request.form['age']
        job = request.form['job']
        cancel = request.form.get('cancel', None)

        try:
            CheckInputIsEmpty(age, job)
        except Exception as err:
            return json.dumps({'is_ok': False, 'error': str(err)})
            # return redirect(url_for('update', username=username))
        else:
            update_information(username, age, job)

            return json.dumps({'is_ok': True, 'error': ''})
            # return redirect(url_for('user'))

# 登出操作
@app.route('/signout/<username>/')
@login_required
def signout(username):
    flash('{} has already signed out!'.format(username))
    session.pop('user')
    return redirect(url_for('login'))

# 注销操作
@app.route('/logout/<username>/')
@login_required
def logout(username):
    log_out(username)
    session.pop('user')
    flash("Account: [{}] has already logout!".format(username))
    return redirect(url_for('index'))

# admin用来删除用户
@app.route('/delete/<username>/')
@login_required
def admin_delete(username):
    log_out(username)
    # admin用户删除普通用户不需要考虑session，
    # session.pop(username)
    flash("Account: [{}] has already deleted!".format(username))
    return redirect(url_for('user', username='admin'))

@app.route('/log/', methods=['GET', 'POST'])
def upload():
    flag = 0

    if request.method == 'GET':
        return render_template('log.html')

    if request.method == 'POST':
        file = request.files.get('file', None)
        line = request.form.get('line', None)


        if file:
            path = '/tmp/%s' % file.filename
            file.save(path)
            print "文件上传完成"
            handle_logs(path)
            print('日志已入库')

        try:
            CheckInputIsEmpty(line)
        except Exception as err:
            return redirect(url_for('upload'))
        else:
            rt_list = fetch_result(line)

            return render_template('log.html', rt_list=rt_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)