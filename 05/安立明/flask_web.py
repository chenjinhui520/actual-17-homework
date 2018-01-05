#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask,render_template,redirect,request
import json
from flask import sessions
from def_util import file_to_dict,dict_to_file,auth_user_status,find_user_exits,del_user,get_user_info

app = Flask(__name__)

app.secret_key='asddsa13asd0a9sxhasdbi'

@app.route('/')

def index():
    #sessions['user']=user
    user_list=file_to_dict()
    return render_template('index.html',user_list=user_list)
    #return redirect('/login')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method =='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if auth_user_status(username,password):
            return redirect('/')
        else:
            return render_template('login.html',error_info='用户名或密码错误，请重新登录')
@app.route('/logout')
def logout():
    return redirect('/login')
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    if request.method=='POST':
        add_dict={}
        ret={}
        uname = request.form.get('username')
        upass = request.form.get('upassword')
        uage = request.form.get('age')
        usex = request.form.get('sex')
        if uname=="":
            ret['status'] = 1
            ret['errmsg']='用户名不能为空'
            return json.dumps(ret)
            #return render_template('register.html',error='用户名不能为空')
        if upass=="":
            ret['status'] = 1
            ret['errmsg']='密码不能为空'
            return json.dumps(ret)
            #return render_template('register.html',error='密码不能为空')
        if find_user_exits(uname):
            ret['status'] = 1
            ret['errmsg'] = '用户已存在'
            return json.dumps(ret)
            #return render_template('register.html', error='用户已存在')
        else:
            add_dict={'name':uname,'passwd':upass,'age':uage,'sex':usex}
            dict_to_file(add_dict)
            ret['status']=0
            return json.dumps(ret)

@app.route('/deleteuser')
def delete_user():
    username=request.args.get('ned_delete')
    ret = {}
    if del_user(username):
        ret['status']=0
        return json.dumps(ret)
    else:
        ret['status']=1
        ret['errmsg']='删除失败'
        return json.dumps(ret)
@app.route('/modify_user',methods=['POST','GET'])
def modify_user():
    if  request.method == 'GET':
        username = request.args.get('username')
        return json.dumps(get_user_info(username))
    if request.method == 'POST':
        ret = {}
        uname = request.form.get('username')
        upass = request.form.get('upassword')
        uage = request.form.get('age')
        usex = request.form.get('sex')
        if uname == "":
            ret['status'] = 1
            ret['errmsg'] = '用户名不能为空'
            return json.dumps(ret)
        if upass == "":
            ret['status'] = 1
            ret['errmsg'] = '密码不能为空'
            return json.dumps(ret)
        else:
            del_user(uname)
            add_dict = {'name': uname, 'passwd': upass, 'age': uage, 'sex': usex}
            dict_to_file(add_dict)
            ret['status'] = 0
            return json.dumps(ret)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)



