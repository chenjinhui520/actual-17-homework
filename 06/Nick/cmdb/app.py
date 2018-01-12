#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/15日16点30分
from flask import Flask,request,render_template,redirect,session,flash,abort
from log2db import log2db
from functools import wraps

import userdb as user
# import user


import os

app = Flask(__name__)
# app.secret_key = os.urandom(32)
app.secret_key = 'asdfasd'


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/user', methods=['GET','POST'])
def hello_user():
    return 'hello user'

@app.route('/users/<uid>')
def user_id(uid):
    return 'hello user: %s'%uid

@app.route('/query_user')
def query_user():
    uid = request.args.get('uid')
    return 'hello user:%s'% uid

# 登录验证装饰器
def auth_login(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if not session:
            return redirect('/login/')
        ret = func(*args,**kwargs)
        return ret
    return inner

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


# 日志列表
@app.route('/logs')
@auth_login
def logs():
    topn = request.args.get('topn','')
    topn = int(topn) if str(topn).isdigit() else 10
    # b if a else c; if判断a，True则执行a，False则执行c
    title = 'LogTop%s' % topn
    log_file = '../access.txt'
    rt_list = log2db(log_file=log_file,topn=topn)
    return render_template('logs.html',rt_list=rt_list, title=title)

# 用户登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username') # 获取用户提交的"username"参数
    password = params.get('password') # 获取用户提交的"password"参数

    if request.method == 'GET':
        return render_template('login.html')
    else:
        if user.validate_login(username,password):
            session['user'] = {'username':username}
            return redirect('/user/list/')
        else:
            return render_template('login.html',username=username, error=u'用户名或密码错误!')

# 用户信息列表
@app.route('/user/list/')
@auth_login
def user_list():
    user_list = user.get_users()
    return render_template('user_list.html',user_list=user_list)


# 添加用户
@app.route('/user/add/',methods=['GET','POST'])
@auth_login
def user_add():
    # 第一步：获取用户填写信息
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username') # 获取用户提交的"username"参数
    password = params.get('password') # 获取用户提交的"password"参数
    age = params.get('age') # 获取用户提交的"password"参数
    job = params.get('job') # 获取用户提交的"password"参数

    if request.method == 'GET':
        return render_template('user_add.html')
    else:
        # 第二步：判断用户是否存在，存在则提示，不存在则添加到user.json文件里
        if user.validate_find(username):
            flash(u'用户名存在，请重新输入')
            return render_template('user_add.html')
        elif not username or not age or not password:
            flash(u'(用户名、年龄、密码)不能为空，请重新输入')
            return render_template('user_add.html')
        else:
            try:
                if user.add_users(username=username, age=age, password=password,job=job):
                    flash(u'添加：%s 成功'%username)
                    return redirect('/user/list/')
                else:
                    return '用户添加失败！'
            except:
                abort(404)


# 用户删除
@app.route('/user/delete/')
@auth_login
def user_delete():
    username = request.args.get('username', '')
    uid = request.args.get('uid', '')
    if user.del_users(uid):
        flash(u'删除：%s 成功'%username)
        return redirect('/user/list/')
    else:
        return '用户删除失败！'


# 更新用户
@app.route('/user/update/',methods=['GET','POST'])
@auth_login
def user_update():
    # 获取用户更新信息，username作为唯一标识符，且不能更新
    username = request.args.get('username', '')
    uid = request.args.get('uid', '')
    age = request.form.get('age', '')
    job = request.form.get('job', '')
    password = request.form.get('password', '')
    # 更新操作代码块
    print uid
    if request.method == 'GET':
        # 用户信息回显
        user_dict = user.get_user(username)[0]
        return render_template('user_upd.html',username=username, user_dict=user_dict)
    else:
        if not username or not password:
            return render_template('user_upd.html', error=u'(密码)不能为空，请重新输入')
        elif user.update_users(username=username, age=age, password=password,job=job,uid=uid):
            flash(u'更新：%s 成功'%username)
            return redirect('/user/list/')
        else:
            return "用户更新失败！"


# 用户登出
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081, debug=True)