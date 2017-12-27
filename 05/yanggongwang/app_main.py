# encoding: utf-8
from flask import Flask,request,render_template,redirect
from users import get_user,vilidata_isUser,add_user,check_user_input,check_user_password,del_user,change_password,disable_user

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# 展示所有的用户账号信息
@app.route('/user/list')
def userList():
    user_list = get_user()
    return render_template('user_list.html', user_list=user_list)

# 新增账号
@app.route('/user/add/',methods=['GET','POST'])
def addUser():
    if request.method == 'GET':
        return render_template('add_user.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password1 = request.form.get('passwd1')
        password2 = request.form.get('passwd2')
        age = request.form.get('age')
        job = request.form.get('job')
        if vilidata_isUser(name):
            # return render_template('add_user.html',error=u'用户已存在！')
            print vilidata_isUser(name)
            return render_template('add_user.html', error=u'用户名存在，请重新输入')
        elif not check_user_input(username=name,password1=password1,password2=password2):
            return render_template('add_user.html', error=u'用户名、密码是必填项！')
        elif not check_user_password(passwd1=password1,passwd2=password2):
            return render_template('add_user.html', error=u'两次输入的密码不一致！')
        else:
            add_user(name=name, passwd=password1, job=job, age=age)
            return render_template('add_user.html',error=u'注册成功！')

# 删除账号
@app.route('/user/del/',methods=['GET','POST'])
def delUser():
    if request.method == 'GET':
        return render_template('del_user.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        if name == '':
            return render_template('del_user.html', error=u'您必须输入要删除的用户名！')
        else:
            if del_user(name):
                return render_template('del_user.html',error=u'%s删除成功！'%(name))
            else:
                return render_template('del_user.html', error=u'%s用户信息删除失败！'%(name))

# 禁用账号
@app.route('/user/disable/',methods=['GET','POST'])
def disableUser():
    if request.method == 'GET':
        return render_template('disable_user_info.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        if name == '':
            return render_template('disable_user_info.html', error=u'您必须输入要停用的用户账号名！')
        else:
            if disable_user(name):
                return render_template('disable_user_info.html',error=u'%s账号停用成功！'%(name))
            else:
                return render_template('disable_user_info.html', error=u'%s账号停用失败！'%(name))

# 修改密码
@app.route('/user/changepwd/',methods=['GET','POST'])
def changePassword():
    if request.method == 'GET':
        return render_template('change_password.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == '':
            return render_template('change_password.html', error=u'您必须输入要停用的用户账号名！')
        else:
            if change_password(name,password):
                return render_template('change_password.html',error=u'%s账号密码修改成功！'%(name))
            else:
                return render_template('change_password.html', error=u'%s账号密码修改失败！'%(name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)


