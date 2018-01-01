# -*- coding:utf8 -*-

from flask import Flask, request, render_template, redirect
from datetime import datetime
from func import *
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # return "hello world"
    return render_template('index.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    users = userdata('users.pickle')

    if request.method == 'GET':
        return render_template('register.html', username="Username",
                               password="Password", retype_password="Retype password" )
    # 获取表单里的用户注册信息
    new_user= request.form.get('username')
    new_password = request.form.get('password')
    retype_password = request.form.get('retype_password')

    try:
        UsernameIsEmpty(new_user)
        CheckPasswordLen(new_password)
        DoubleCheckPassword(new_password, retype_password)
        UsernameAlreadyExist(new_user, users)
    except Exception as err:
        key = get_key(err.args[0])
        dicterr = get_dicterr(err.args[0])
        return render_template('register.html', username=dicterr.get('username'),
                               password=dicterr.get('password'),
                               retype_password=dicterr.get('retype_password'),
                               style_input = key,
                               color="red" )
    else:
        users[new_user] = new_password
        userdata('users.pickle', users)


        return render_template('prompt.html')

@app.route("/login/", methods=['GET', 'POST'])
def login():
    users = userdata('users.pickle')

    login_user = request.form.get('username')
    login_password = request.form.get('password')

    if request.method == 'GET':
        return render_template('login.html')

    try:
        CheckLoginIn(login_user, login_in)
        CheckLoginUser(login_user, users)
        CheckPassword(login_user, login_password, users)
    except Exception as err:
        return render_template('login.html', login_error=err)
    else:
        # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        login_in[login_user] = 'online'

        return redirect('/user/?cuser={0}'.format(login_user))

@app.route('/user/')
def user():
    user_status = {}
    information = ''
    # 获取已注册用户
    users = userdata('users.pickle')
    # 标识当前用户
    current_user = request.args.get('cuser')

    # 时刻关注用户是否登陆
    if current_user not in login_in:
        return render_template('error.html', current_user=current_user)

    # 返回管理员界面
    if current_user == 'admin':
        # 显示被删除的用户
        delete_user = request.args.get('delete')
        # 这一条是为了防止第一次进入admin界面时，出现用户被删除的提示
        if delete_user == None:
            information = ''
        else:
            information = "{} has already deleted".format(delete_user)

        # 获取当前用户登陆状态
        for key in users:
            if key == 'admin':
                continue
            user_status[key] = login_in.get(key, 'offline')

        return render_template('admin.html', user_status=user_status,
                           current_user=current_user,
                           information=information)
    else:
        # 普通用户界面
        filename = "{}.pickle".format(current_user)
        current_user_data = userdata(filename)
        print current_user_data
        return render_template('user.html', current_user=current_user, current_user_data=current_user_data)




@app.route('/user/delete/')
def delete():
    users = userdata('users.pickle')
    current_user = request.args.get('cuser')

    # 时刻关注用户是否还在登陆
    if current_user not in login_in:
        return render_template('error.html', current_user=current_user)

    # 需要复用这个url，当用户是admin时用来删除用户，当为其他用户时，用来删除用户指定数据
    # 普通用户url为/user/delete?cuser=普通用户&dtitle=要删除的标题
    if current_user == 'admin':
        duser = request.args.get('duser')

        if duser in login_in:
            del login_in[duser]
        del users[duser]

        userdata('users.pickle', users)
        # 删用户关联的数据
        duser_file = '{}.pickle'.format(duser)
        if os.path.exists(duser_file):
            os.remove(duser_file)
        return redirect('/user/?cuser={0}&delete={1}'.format(current_user, duser)) # information="{} has already deleted".format(username))
    else:
        # 遇到问题：第一条数据删不掉--->已解决，是userdata逻辑错误
        dtitle = request.args.get('dtitle')
        current_user_file = '{}.pickle'.format(current_user)
        user_data = userdata(current_user_file)

        del user_data[dtitle]
        user_data = {}
        userdata(current_user_file, user_data)
        print userdata(current_user_file)
        # 返回的delete带中文会报错
        # return redirect('/user/?cuser={0}&delete={1}'.format(current_user, dtitle))
        return redirect('/user/?cuser={0}'.format(current_user))
# 注销操作
@app.route('/signout/')
def signout():
    current_user = request.args.get('cuser')

    # 时刻关注用户是否还在登陆状态
    if current_user not in login_in:
        return render_template('error.html', current_user=current_user)

    del login_in[current_user]

    return redirect('/')


# 用来添加用户的blog
@app.route('/test/', methods=['GET', 'POST'])
def test():
    # 获取当前用户
    current_user = request.args.get('cuser')

    # 时刻确认用户是否还在登陆状态
    if current_user not in login_in:
        return render_template('error.html', current_user=current_user)

    # 获取当前用户数据
    filename = "{}.pickle".format(current_user)
    current_user_data = userdata(filename)

    if request.method == 'GET':
        return render_template('test.html')

    title = request.form.get('title')
    comment = request.form.get('comment')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 写入该用户数据
    current_user_data[title] = [comment, current_time]
    # 该用户的数据文件
    filename = "{}.pickle".format(current_user)

    userdata(filename, current_user_data)

    return redirect('/user?cuser={}'.format(current_user))
    # 对user.html无效
    # return redirect('/')

if __name__ == '__main__':
    login_in = {}
    app.run(host='0.0.0.0', port=8081, debug=True)
