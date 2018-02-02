# encoding: utf-8
from flask import request,render_template,redirect, session, flash
from  log2db import GetTopN
from functools import wraps
import userdb as user
import assets
import json

from . import app


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


@app.route('/logs/', methods=['POST','GET'])
@login_required
def logs():
    files = request.files.get('files')
    if files:
        files.save('./access.txt')
        log_file = 'access.txt'
        if GetTopN(log_file, fetch=False):
            return redirect('/logs/')
        else:
            return '日志写入数据库失败！'
    else:
        topn = request.form.get('topn')
        # 三目表达式
        topn = int(topn) if str(topn).isdigit() else 10
        title = 'Reboot'
        log_file = 'access.txt'
        log_list = GetTopN(log_file, topN=topn, fetch=True)
        return render_template('logs.html', title=title, logall_list=log_list)

# 用户登陆
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

# 用户登出
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')


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

# 更新用户信息
@app.route('/user/update/',methods=['POST','GET'])
@login_required
def user_update():
    perams = request.args if request.method == 'GET'else request.form
    uid = perams.get('uid','')
    age = perams.get('age','')
    job = perams.get('job','')
    _user = user.get_user_by_id(uid=uid)[0]
    if request.method == 'GET':
        return json.dumps(_user)
    else:
        #1、验证用户数据合法性；
        _is_ok, error = user.vilidate_update_user(uid=uid,age=age,job=job)
        if _is_ok:
            # 2、如果合法，入库；
            flash(u'更新: %s成功' % _user['username'])
            user.user_update(uid, age, job)
        return json.dumps({'is_ok': _is_ok, 'error': error})


# 更新用户密码
@app.route('/user/change-passwd/',methods=['POST'])
@login_required
def change_passwd():
    userid = request.form.get('userid')
    user_passwd = request.form.get('user-passwd')
    manager_passwd = request.form.get('manager-passwd')
    _is_ok, error = user.vilidate_change_user_passwd(userid, user_passwd,session['user']['username'],manager_passwd)
    if _is_ok:
        # 更新用户密码
        user.change_user_passwd(userid,user_passwd)
    return json.dumps({'is_ok':_is_ok,'error':error})


#############资产管理###############

# 资产信息列表
@app.route('/asset/list/',methods=['GET'])
@login_required
def asset_list():
    asset_list = assets.get_list()
    return render_template('asset/asset_list.html',asset_list=asset_list)


# 创建资产信息
@app.route('/asset/create/',methods=['POST','GET'])
@login_required
def asset_create():
    perams = request.args if request.method == 'GET'else request.form
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
    asset_dict = {}
    for i in lists:
        asset_dict['_'+i] = perams.get(i)
    if request.method == 'GET':
        return render_template('asset/asset_create.html',idcs=assets.get_idc())
    else:
        # 1、验证用户数据合法性；
        _is_ok, msg = assets.vilidate_create_asset(asset_dict)
        # 2、如果合法，入库；
        if _is_ok:
            # 数据入库
            _is_ok, msg = assets.create_asset(asset_dict)
        return json.dumps({'is_ok': _is_ok, 'msg': msg})
# 更新资产信息
@app.route('/asset/update/',methods=['POST','GET'])
@login_required
def asset_update():
    perams = request.args if request.method == 'GET'else request.form
    aid = perams.get('aid','')
    if request.method=='GET':
        return render_template('asset/asset_update.html',assets=assets.update_select(aid),idcs=assets.get_idc())
    if request.method=='POST':
        lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os','id']
        asset_dict = {}
        for i in lists:
            asset_dict['__'+i] = perams.get(i)
        # 1.验证合法性
        _is_ok, msg = assets.vilidate_update_asset(asset_dict)
        # 2、如果合法，更新；
        if _is_ok:
            # 数据入库
            _is_ok, msg = assets.update_asset(asset_dict)
        return json.dumps({'is_ok': _is_ok, 'msg': msg})

# 删除用户资产
@app.route('/asset/delete/',methods=['GET'])
@login_required
def asset_delete():
    asset_sn = request.args.get('sn', '')
    aid = request.args.get('aid', '')
    if assets.delete_asset(aid):
        flash(u'删除: %s成功' % asset_sn)
        return redirect('/asset/list/')
    else:
        return '资产删除失败.'