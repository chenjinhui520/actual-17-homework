# -*- coding:utf8 -*-
from flask import Flask, request, render_template, \
    redirect, flash, url_for, session

from db_utlis import *
from check_utils import *
from functools import wraps

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

@app.route('/')
def index():
    return render_template('index.html')

# 用户登录
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
            session['username'] = username
            return redirect(url_for('user', username=username))

# 用户注册
@app.route('/register/', methods=['GET', 'POST'])
def register():

    name = request.args.get('name', None)

    if request.method == 'GET':
        return render_template('register.html', name=name)

    if request.method == 'POST':
        users = fetch_users()
        # print(users)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        retype_password = request.form.get('retype_password', None)
        age = request.form.get('age',None)
        job = request.form.get('job', None)

        try:
            # 用户信息禁止为空
            CheckInputIsEmpty(username, age, job)
            # 密码长度检测
            CheckPasswordLen(password)
            # 二次验证密码
            DoubleCheckPassword(password, retype_password)
            # 用户名是否已注册
            UsernameAlreadyExist(username, users)

        except Exception as err:
            # err是json格式？
            # 之前没加str()时，except是不执行的！Fuck!
            flash(str(err))
            return redirect(url_for('register'))
        else:
            add_user(username, password, age, job)

            # admin用户可以添加新用户，需要复用register
            # 因此区分操作来源
            # 用户自行注册
            if not name:
                flash('Register  successfully!')
                return redirect(url_for('index'))
            # admin添加新用户
            else:
                # 这个用format去格式化中文会报错！！！
                flash('Add a new user: [%s]' % username)
                return redirect(url_for('user', username=name))

# 用户页面
@app.route('/user/<username>/')
@login_required
def user(username):
    flash('Welcome back {}!'.format(username))

    # 用户为admin，需要获取全部用户数据
    if username == 'admin':
        user_dict = fetch_all_information()
    else:
        # 获取当前登录用户数据
        user_dict = fetch_information(username)
        print user_dict
    return render_template('user.html', username=username, user_dict=user_dict)

# 密码修改
# 密码修改页面是通用的，唯一的不同就是修改完成后的返回页面
# 因此使用两条路由共用一个处理函数

@app.route('/change/<username>/', methods=['GET', 'POST'])
@app.route('/user/admin/change/<username>/', methods=['GET', 'POST'])
@login_required
def change(username):
    if request.method == 'GET':

        return render_template('change.html', username=username)

    # 获取当前的path，用来区分是admin还是普通用户


    if request.method == 'POST':
        path = request.path
        print path

        cupassword = request.form['cupassword']
        nepassword = request.form['nepassword']
        repassword = request.form['repassword']
        cancel = request.form.get('cancel', None)

        # 取消密码修改
        if cancel == 'Cancel':
            if 'admin' in path:
                return redirect(url_for('user', username='admin'))
            else:
                return redirect(url_for('user', username=username))
        else:
            try:
                # 密码验证
                CheckLogin(username, cupassword)
                # 密码长度检测
                CheckPasswordLen(nepassword)
                # 二次严重那个
                DoubleCheckPassword(nepassword, repassword)

            except Exception as err:
                flash(str(err))
                return redirect(path)
            else:
                change_password(username, nepassword)
                flash('[%s]: Password has changed successfully!' % username)
                # 根据path里是否有admin来决定如何跳转的

                if 'admin' in path:
                    return redirect(url_for('user', username='admin'))
                else:
                    return redirect(url_for('user', username=username))

# 用户数据更新，思路和change一样，代码很相似
@app.route('/update/<username>/', methods=['GET', 'POST'])
@app.route('/user/admin/update/<username>/', methods=['GET', 'POST'])
@login_required
def update(username):
    user_dict = fetch_information(username)

    if request.method == 'GET':
        return render_template('update.html', username=username, user_dict=user_dict)

    path = request.path

    if request.method == 'POST':
        # admin对用户数据进行修改的代码和注册是一样的，怎么优化？

        user_dict = fetch_information(username)
        age = request.form['age']
        job = request.form['job']
        cancel = request.form.get('cancel', None)

        if cancel == "Cancel":
            if 'admin' in path:
                return redirect(url_for('user', username='admin'))
            else:
                return redirect(url_for('user', username=username))

        else:
            try:
                CheckInputIsEmpty(age, job)
            except Exception as err:
                flash(str(err))
                return redirect(url_for('update', username=username))
            else:
                update_information(username, age, job)
                flash('Information update successfully!')
                if 'admin' in path:
                    return redirect(url_for('user', username='admin'))
                else:
                    return redirect(url_for('user', username=username))

@app.route('/log/admin/', methods=['GET', 'POST'])
@login_required
def log():
    if request.method == 'GET':
        return render_template('log.html')

    if request.method == 'POST':
        log = request.form.get('log', None)
        cancel = request.form.get('cancel', None)

        if cancel == 'Cancel':
            return redirect(url_for('user', username='admin'))

        else:
            try:
                CheckInputIsEmpty(log)
            except Exception as err:
                flash(str(err))
                return redirect(url_for('log'))
            else:
                log_list = fetch_log(log)
                return render_template('exhibition.html', log_list=log_list)

# 登出操作
@app.route('/signout/<username>/')
@login_required
def signout(username):
    flash('{} has already signed out!'.format(username))
    return redirect(url_for('login'))

# 注销操作
@app.route('/logout/<username>/')
@login_required
def logout(username):
    log_out(username)
    session.pop('username')
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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)