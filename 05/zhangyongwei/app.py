#!/usr/bin/env python
#coding:utf8
from flask import Flask,request,render_template,redirect
from top import getTopN
import user
app = Flask(__name__)

@app.route('/')
def hello_world():
    topn = request.args.get('topn')
    topn = int(topn) if str(topn).isdigit() else 10
    context =  getTopN('access.txt',topN=topn)
    return render_template('index.html',title='log_topn', lines = context)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    if user.validate_login(username,password):
        return redirect('/user/list/')
    else:
        return render_template('login.html',username=username,error=u'用户名或密码错误!')

@app.route('/user/list/')
def userlist():
    return render_template('userlist.html', userlist=user.get_user())


@app.route('/user/add/',methods=['POST','GET'])
def useradd():
    if request.method == 'GET':
        return render_template('user_add.html')

    userinfo = request.form.to_dict()
    result = user.insert_user(**userinfo)
    return result

@app.route('/user/update/', methods=['POST','GET'])
def user_update():
    if request.method == 'GET':
        username = request.args.get('username')
        users = user.get_user()
        for i in users:
            if i['name'] == username:
                return render_template('user_update.html',user=i)

    userinfo = request.form.to_dict()
    result = user.update_user(**userinfo)
    return result

@app.route('/user/delete/', methods=['POST', 'GET'])
def user_del():
    username = request.args.get('username')
    users = user.get_user()
    for i in users:
        if i['name'] == username:
            user.del_user(username)
            return redirect('/user/list/')


@app.route('/query_user')
def query_user():
    uid = request.args.get('uid')
    print request.arg.get('uid')
    return query_user()

@app.route('/logs/')
def logs():
    return render_template('logs.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)


