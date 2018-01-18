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


# 登录验证装饰器
def auth_login(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if not session:
            return redirect('/user/login/')
        ret = func(*args,**kwargs)
        return ret
    return inner


@app.route('/')
@auth_login
def hello_world():
    return render_template('public/index_body.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


# 日志列表
@app.route('/logs/', methods=['POST', 'GET'])
@auth_login
def logs():
    files = request.files.get('files')
    if files:
        files.save('./access.txt')
        log_files = 'access.txt'
        if log2db(log_files=log_files, fetch=False):
            return redirect('/logs/')
        else:
            return '日志写入数据库失败！'
    else:
        topn = request.form.get('topn','')
        topn = int(topn) if str(topn).isdigit() else 10
        log_file = '../access.txt'
        rt_list = log2db(log_files=log_file,topn=topn)
        return render_template('logs.html',rt_list=rt_list, title='LogTop%s' % topn)

# 用户登录
@app.route('/user/login/', methods=['GET', 'POST'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username') # 获取用户提交的"username"参数
    password = params.get('password') # 获取用户提交的"password"参数

    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        if user.validate_login(username,password):
            session['user'] = {'username':username}
            return redirect('/user/list/')
        else:
            return render_template('user/login.html',username=username, error=u'用户名或密码错误!')

# 用户信息列表
@app.route('/user/list/')
@auth_login
def user_list():
    user_list = user.get_users()
    return render_template('user/user_list.html',user_list=user_list)


# 添加用户
@app.route('/user/add/',methods=['GET','POST'])
@auth_login
def user_add():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    password = params.get('password')
    age = params.get('age')
    job = params.get('job')
    if request.method == 'GET':
        return render_template('user/user_add.html')
    else:
        is_ok, error = user.validate_add_user(username=username, age=age, password=password,job=job)
        if is_ok:
            user.add_users(username=username, age=age, password=password, job=job)
            flash(u'添加：%s 成功' % username)
            return redirect('/user/list/')
        else:
            return render_template('user/user_add.html', error=error)

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
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('uid', '')
    age = params.get('age', '')
    job = params.get('job', '')
    password = params.get('password', '')
    # 根据ID获取用户信息
    user_dict = user.get_user(uid)
    if request.method == 'GET':
        return render_template('user/user_modify.html',user_dict=user_dict)
    else:
        is_ok, error = user.validate_update_user(uid=uid,password=password,age=age,job=job)
        if is_ok:
            user.update_users(uid=uid, password=password, age=age, job=job)
            flash(u'更新：%s 成功' % user_dict.get('username'))
            return redirect('/user/list/')
        else:
            return render_template('user/user_modify.html', user_dict=user_dict, error=error)

# 用户登出
@app.route('/user/logout/')
def logout():
    session.clear()
    return redirect('/user/login/')


@app.route('/test/', methods=['POST', 'GET'])
def test():
    return render_template('test.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8007, debug=True)