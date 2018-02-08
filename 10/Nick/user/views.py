#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/15日16点30分
from flask import Flask,request,render_template,redirect,session,flash,abort
from log2db import log2db
from functools import wraps
import json
from user import app
from models import User, Asset

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
        if User.validate_login(username,password):
            session['user'] = {'username':username}
            return redirect('/user/list/')
        else:
            return render_template('user/login.html',username=username, error=u'用户名或密码错误!')

# 用户信息列表
@app.route('/user/list/')
@auth_login
def user_list():
    user_list = User.get_list()
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
        # 实例化用户类
        _user = User(id=None,username=username, age=age, password=password,job=job)
        is_ok, error = _user.validate_add_user()
        if is_ok:
            _user.save()
        return json.dumps({'is_ok': is_ok, 'error': error})

# 用户删除
@app.route('/user/delete/')
@auth_login
def user_delete():
    username = request.args.get('username', '')
    uid = request.args.get('uid', '')
    if User.del_users(uid):
        flash(u'删除：%s 成功'%username)
        return redirect('/user/list/')
    else:
        return '用户删除失败！'


# 更新用户信息
@app.route('/user/update/',methods=['GET','POST'])
@auth_login
def user_update():
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('uid', '')
    age = params.get('age', '')
    job = params.get('job', '')
    # 根据ID获取用户信息
    user_dict = User.get_user(uid)
    if request.method == 'GET':
        return json.dumps(user_dict)
    else:
        # 实例化用户类
        _user = User(id=uid,age=age,job=job,username=None,password=None)
        is_ok, error = _user.validate_update_user()
        if is_ok:
            _user.update()
            flash(u'更新：%s 成功' % user_dict.get('username'))
        return json.dumps({'is_ok': is_ok, 'error': error})

# 更新用户密码
@app.route('/user/charge-passwd/', methods=['POST'])
@auth_login
def charge_passwd():
    print request.form
    uid = request.form.get('userid')
    manage_passwd = request.form.get('manage_passwd')
    user_passwd = request.form.get('user_passwd')
    is_ok, error = User.validate_cherge_user_passwd(uid,user_passwd,session['user']['username'], manage_passwd)
    msg = ''
    if is_ok:
        User.cherge_user_passwd(uid,user_passwd)
        msg = '用户密码更新成功!'
    return json.dumps({'is_ok':is_ok, 'error':error,'msg':msg})


# 用户登出
@app.route('/user/logout/')
def logout():
    session.clear()
    return redirect('/user/login/')




###############################【资产路由中心】#################################

# 资产信息列表
@app.route('/asset/list/')
@auth_login
def asset_list():
    _asset_list = []
    for i in Asset.get_list():
        _rt_list = Asset.get_by_id(i.get('idc_id'))
        i['idc_id'] = _rt_list[0][1]
        _asset_list.append(i)
    return render_template('asset/asset_list.html',asset_list=_asset_list)


# 添加资产信息
@app.route('/asset/add/', methods=['POST', 'GET'])
@auth_login
def asset_add():
    if request.method == 'GET':
        return render_template('asset/asset_create.html', idcs=Asset.get_idc())
    else:
        lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','os','cpu','ram','disk']
        asset_dict = {}
        for i in lists:
            asset_dict['_'+i] = request.form.get(i, '')
        # 检查资产信息
        is_ok, error = Asset.validate_create(asset_dict)
        msg = ''
        status = 0
        if is_ok:
            if Asset.save(asset_dict):
                msg = '添加资产成功！'
                status = 0
            else:
                msg = '添加资产失败！'
                status = 1
        return json.dumps({'is_ok': is_ok, 'status': status, 'msg': msg, 'error': error})

# 删除资产信息
@app.route('/asset/delete/')
@auth_login
def asset_delete():
    asset_id = request.args.get('aid', '')
    if Asset.delete(asset_id):
        return redirect('/asset/list/')
    else:
        return '资产删除失败！'


# 更新资产信息
@app.route('/asset/update/', methods=['POST', 'GET'])
@auth_login
def asset_update():
    if request.method == 'GET':
        # 返回更新资产模版给dialog页面
        _id = request.args.get('aid', '')
        _asset_list = []
        for i in Asset.get_list():
            if i.get('id') == int(_id):
                _asset_list.append(i)
        return render_template('asset/asset_update.html', asset_list=_asset_list, idcs=Asset.get_idc())
    else:
        lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','os','cpu','ram','disk','id']
        asset_dict = {}
        for i in lists:
            asset_dict['_'+i] = request.form.get(i, '')
        # 检查资产信息
        is_ok, error = Asset.validate_update(asset_dict)
        msg = ''
        status = 0
        if is_ok:
            if Asset.update(asset_dict):
                msg = '更新资产成功！'
                status = 0
            else:
                msg = '更新资产失败！'
                status = 1
        return json.dumps({'is_ok': is_ok, 'status':status, 'msg': msg, 'error': error})