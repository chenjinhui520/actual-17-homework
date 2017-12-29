#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年12月26日

@author: rayleiwj
'''
from flask import Flask,request,render_template,redirect
import user
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title=u'主页')
@app.route('/register')
def register():
    '''注册用户'''
    if request.method=='GET':
        return render_template('register.html')
    elif request.method=='POST':
        username = request.form.get('username')
        age = request.form.get('age')
        job = request.form.get('job')
        userpasswd = request.form.get('userpasswd')
        #判断用户添加是否合法
        is_ok,error = user.vilidata_find(username=username,userpasswd=userpasswd,job=job,age=age)
        if is_ok:
            return render_template('register.html',error=error)
        #用户合法后添加用户
        is_ok,error = user.user_add(username=username,userpasswd=userpasswd,job=job,age=age)
        if is_ok:
            return render_template('register.html',error=error,title=u'注册用户')
        return redirect('/login')
@app.route('/login/',methods=['POST','GET'])
def login():
    '''用户登录'''
    error = None
    if request.method=='POST':
        username = request.form.get('username')
        userpasswd = request.form.get('userpasswd')
        if user.vilidata_user(username, userpasswd):
            return redirect('/user/userlist')
        error = True
    return render_template('login.html',error=error,title=u'用户登录')
@app.route('/user/userlist')
def userlist():
    '''列出所有用户信息'''
    userlist = user.get_user()
    return render_template('userlist.html',userlist=userlist,title=u'用户列表')
@app.route('/user/useradd',methods=['GET','POST'])
def useradd():
    '''添加用户'''
    if request.method=='GET':
        return render_template('useradd.html')
    elif request.method=='POST':
        username = request.form.get('username')
        age = request.form.get('age')
        job = request.form.get('job')
        userpasswd = request.form.get('userpasswd')
        #判断用户添加是否合法
        is_ok,error = user.vilidata_find(username=username,userpasswd=userpasswd,job=job,age=age)
        if is_ok:
            return render_template('useradd.html',error=error)
        #用户合法后添加用户
        is_ok,error = user.user_add(username=username,userpasswd=userpasswd,job=job,age=age)
        if is_ok:
            return render_template('useradd.html',error=error,title=u'添加用户')
        return redirect('/user/userlist')
@app.route('/user/del',methods=['POST','GET'])
def userdel():
    '''删除用户'''
    user_list = user.get_user()    
    if request.method=='GET':
        deluser = request.args.get('deluser')
        user.user_del(deluser)
        return redirect('/user/userlist')
@app.route('/user/update',methods=['POST','GET'])
def userupdate():
    if request.method=='GET':
        user_up = request.args.get('userupdate')
        return render_template('userupdate.html',user_up=user_up)
    if request.method=='POST':
        user_up = request.form.get('username')
        age = request.form.get('age')
        job = request.form.get('job')
        userpasswd = request.form.get('userpasswd')
        is_ok,error = user.user_update(user_up, userpasswd, job, age)
        if is_ok:
            return render_template('userupdate.html',user_up=user_up,error=error)
        return redirect('/user/userlist')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)