# encoding: utf-8

import gconf
import json


# 获取所有用户信息
def get_user():
    try:
        handler = open(gconf.USER_FILE,'r')
        cxt = handler.read()
        handler.close()
        return json.loads(cxt)
    except:
        return []

# 登陆时验证用户名和密码
def vilidate_login(username,password):
    all_user = get_user()
    for user in all_user:
        if user.get('name') == username and user.get('passwd') == password:
            return True
    return False


def vilidate_find(name,passwd,age,job):
    all_user = get_user()
    for user in all_user:
        if user.get('name') == name:
            return True, u'用户已存在.'
    if not name:
        return True, u'用户名不能为空'
    if not passwd:
        return True, u'密码不能为空'
    if not age:
        return True, u'年龄不能为空'
    if not job:
        return True, u'职务不能为空'
    return False, ''

def add_user(name,passwd,age,job):
    try:
        newUser = {'name':name,'passwd':passwd,'age':age,'job':job}
        srcUser = get_user()
        srcUser.append(newUser)
        newUser = json.dumps(srcUser)
        handler = open(gconf.USER_FILE, 'w')
        handler.write(newUser)
        handler.close()
        return True
    except:
        return False


def user_delete(username):
    srcUser = get_user()
    # 通过用户名找到索引位置
    if srcUser:
        index = 0
        for user in srcUser:
            if user.get("name") == username:
                break
            index += 1
    else:
        return False
    try:
        srcUser.pop(index)
        handler = open(gconf.USER_FILE, 'w')
        handler.write(json.dumps(srcUser))
        handler.close()
        return True
    except:
        return False


def get_user_by_name(username):
    srcUser = get_user()
    rt_dict = {}
    for user in srcUser:
        if user.get("name") == username:
            rt_dict = user
    return rt_dict


def user_update(username,passwd,age,job):
    srcUser = get_user()
    # 通过用户名找到索引位置
    if srcUser:
        index = 0
        for user in srcUser:
            if user.get("name") == username:
                break
            index += 1
    else:
        return False
    try:
        newUser = srcUser.pop(index)
        newUser['passwd'] = passwd
        newUser['age'] = age
        newUser['job'] = job
        srcUser.append(newUser)
        newUser = json.dumps(srcUser)
        handler = open(gconf.USER_FILE, 'w')
        handler.write(newUser)
        handler.close()
        return True
    except:
        return False


if __name__=='__main__':
    # print get_user()
    # print vilidate_login('wd','wd')
    print get_user_by_name('wd')
