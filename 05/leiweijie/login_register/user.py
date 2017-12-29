#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年12月26日

@author: rayleiwj
'''
import gconf
import json
def get_user():
    '''获取所有用户信息'''
    with open(gconf.DB_FILE,'r') as f:
        user_list = json.loads(f.read())
        return user_list
def vilidata_user(username,userpasswd):
    '''验证用户名密码时候相等'''
    user_list = get_user()
    for i in user_list:
        if i.get('name')==username and i.get('passwd')==userpasswd:
            return True
    return False
def vilidata_find(username,userpasswd,job,age):
    '''验证用户名、密码、工作、年龄是否合法'''
    userlist = get_user()
    for i in userlist:
        if i.get('name')==username:
            return True,u'用户名已存在请重新添加！'
    if not userpasswd:
        return True,u'密码不能为空！'
    elif not job:
        return True,u'工作不能为空！'
    elif not age:
        return True,u'年龄不能为空！'
    return False, '' 
def vilidata_find_other(userpasswd,job,age):
    '''验证密码、工作、年龄是否合法'''
    if not userpasswd:
        return True,u'密码不能为空！'
    elif not job:
        return True,u'工作不能为空！'
    elif not age:
        return True,u'年龄不能为空！'
    return False, '' 
def user_add(username,userpasswd,job,age):
    '''添加用户'''
    try:
        userlist = get_user()
        new_user = {'name':username,'passwd':userpasswd,'job':job,'age':int(age)}
        userlist.append(new_user)
        save_user(userlist)
        return False,u'用户添加成功！'
    except:
        return False,u'用户添加失败！'
    
def save_user(userlist):
    '''将用户保存到文件中'''
    with open(gconf.DB_FILE,'w') as f:
        f.write(json.dumps(userlist))
def user_del(username):
    '''利用用户的索引值删除用户信息'''
    userlist = get_user()
    user_index = 0
    for users in userlist:
        if users['name']==username:
            del userlist[user_index]
        user_index +=1
    save_user(userlist)
def user_update(user_up,userpasswd, job, age):
    userlist = get_user()
    user_index = 0
    for users in userlist:
        if users['name']==user_up:
            is_ok,error = vilidata_find_other(userpasswd, job, age)
            if is_ok:
                return error
            new_user = {'name':user_up,'passwd':userpasswd,'job':job,'age':int(age)}
            userlist[user_index]=new_user
        user_index +=1
    save_user(userlist)
if __name__ == '__main__':
    pass