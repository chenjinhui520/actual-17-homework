# encoding: utf-8
from flask import Flask, request,render_template,redirect, session, flash
from  Log_Analysis import GetTopN
from functools import wraps
import userdb as user
import json
import assets

# app = Flask(__name__)
# app.secret_key = '13123dfasdf'

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
    title = '51Reboot'
    content = ['hello Nick','hello Reboot']
    # return render_template('index.html',contents=content)
    return render_template('public/index_body.html',contents=content)


@app.route('/logs/')
@login_required
def logs():
    topn = request.args.get('topn')
    # 三目表达式
    topn = int(topn) if str(topn).isdigit() else 10
    title = 'Reboot'
    # log_file = 'access.txt'
    # log_list =  GetTopN(log_file, topN=topn)
    log_list = user.get_accesslog(topn)
    return render_template('user/logs.html',title=title,logall_list=log_list )


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
    file = request.files.get('file')
    if file:
        file.save("/tmp/%s" % file.filename)
    if request.method == 'GET':
        return render_template('user/user_add.html')
    elif request.method == 'POST':
        _is_ok, error = user.vilidate_find(name,passwd,age,job)
        if _is_ok:
            # flash(error)
            # return render_template('user/user_add.html')
            return json.dumps({"is_ok":_is_ok, "error":error})
        else:
            if user.add_user(name,passwd,age,job):
                # flash(u'添加: %s成功'%name)
                # return redirect('/user/list/')
                return json.dumps({"is_ok":_is_ok, "error":error})
            else:
                # return render_template('user/user_add.html', error=u'用户写入失败.')
                return json.dumps({"is_ok":_is_ok, "error":error})


@app.route('/user/delete/',methods=['GET'])
@login_required
def user_delete():
    username = request.args.get('uid', '')
    if user.user_delete(username):
        flash(u'删除: %s成功' % username)
        return redirect('/user/list/')
    else:
        return '用户删除失败.'

@app.route('/user/update/',methods=['POST','GET'])
@login_required
def user_update():
    perams = request.args if request.method == 'GET'else request.form
    uid = perams.get('uid','')
    # passwd = perams.get('passwd','')
    age = perams.get('age','')
    job = perams.get('job','')
    print uid,age,job
    _user = user.get_user_by_id(uid=uid)[0]
    if request.method == 'GET':
        return render_template('user/user_update.html',_user=_user)
    if user.user_update(uid,age,job):
        # flash(u'更新: %s成功' %_user['username'])
        # return redirect('/user/list/')
        return json.dumps({"is_ok": True, "msg":u"更新%s成功" % _user['username']})
    else:
        # return '用户更新失败.'
        return json.dumps({"is_ok": False, "msg":u"更新%s失败" % _user['username']})

@app.route('/user/change-passwd/', methods=['POST'])
@login_required
def change_passwd():
    userid = request.form.get('userid')
    user_passwd = request.form.get('user-passwd')
    manager_passwd = request.form.get('manager-passwd')
    is_ok,error = user.vilidate_change_user_passwd(userid,user_passwd,session['user']['username'],manager_passwd)
    if is_ok:
        user.change_user_passwd(userid,user_passwd)
    return json.dumps({"is_ok":is_ok, "error":error})


# 用户登出
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')

@app.route('/test/')
def test():
    return render_template('test.html')

@app.route('/asset/list/')
def asset_list():
    asset_list = assets.get_list()
    idcs = dict(assets.get_idc())
    for asset in asset_list:
        asset['idc_name'] = idcs[asset['idc_id']]
    return render_template('/asset/asset_list.html', asset_list=asset_list)


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
        _is_ok, error = assets.vilidate_create_asset(asset_dict)
        # 2、如果合法，入库；
        if _is_ok:
            # 数据入库
            assets.create_asset(asset_dict)
            return json.dumps({'is_ok': _is_ok, 'error': u'资产添加成功'})
        else:
            return json.dumps({'is_ok': _is_ok, 'error': error})


@app.route('/asset/update/', methods=['POST','GET'])
@login_required
def asset_update():
    perams = request.args if request.method == 'GET'else request.form
    sn = perams.get('sn')
    asset = assets.get_asset_by_sn(sn)
    idcs = assets.get_idc()
    for idc in idcs:
        if idc[0] == asset['idc_id']:
            selected = asset['idc_id']
    if request.method == 'GET':
        return render_template('asset/asset_update.html',asset=asset,idcs=idcs,selected=selected)
    else:
        lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
        asset_dict = {}
        for i in lists:
            asset_dict['_'+i] = perams.get(i)
        _is_ok, error = assets.vilidate_update_asset(asset_dict)
        if _is_ok:
            assets.update_asset(sn,asset_dict)
            return json.dumps({'is_ok': _is_ok, 'error': u'资产更新成功'})
        else:
            return json.dumps({'is_ok': _is_ok, 'error': error})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

