#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/15日19点11分
import gconf
import json

# 获取用户列表信息
def get_users():
    try:
        handler = open(gconf.USER_FILE, 'rb')
        cxt = handler.read()
        handler.close()
        return json.loads(cxt)
    except:
        return []

# 获取单个用户信息
def get_user(username):
    users = get_users()
    rt_user = {}
    for user in users:
        if user.get('name') == username:
            rt_user = user
    return rt_user


# 验证用户名和密码是否重复
def validate_login(username, password):
    users = get_users()
    print users
    for user in users:
        if user.get('name') == username and user.get('passwd') == password:
            return True
    return False

# 验证用户名是否重复
def validate_find(username):
    users = get_users()
    for user in users:
        if user.get('name') == username:
            return True
    return False


# 添加用户信息
def add_users(username, age, password, job):
    # 获取新用户数据
    newUser = {'name': username, 'age': int(age), 'passwd': password, 'job':job}
    # 获取旧用户数据
    srcUsers = get_users()
    # 将新旧用户数据添加到一个list列表中，并做json格式转换
    srcUsers.append(newUser)
    # 保存用户
    return save_user(srcUsers)

# 删除用户信息
def del_users(username):
    srcUsers = get_users()
    _isok_, index = get_user_index(srcUsers,username)
    if _isok_:
        srcUsers.pop(index)
        return save_user(srcUsers)
    else:
        return False

# 更新用户信息
def update_users(username, age, password, job):
    srcUsers = get_users()
    _isok_, index = get_user_index(srcUsers,username)
    if _isok_:
        upUser = srcUsers.pop(index)
        upUser['age'] = int(age)
        upUser['job'] = job
        upUser['passwd'] = password
        # 将更新的新用户数据加入到源数据列表
        srcUsers.append(upUser)
        # 保存用户
        return save_user(srcUsers)
    else:
        return False

#######代码优化部分#########
# 保存用户函数
def save_user(srcUsers):
    try:
        handler = open(gconf.USER_FILE, 'wb')
        handler.write(json.dumps(srcUsers))
        handler.close()
        return True
    except:
        return False

def get_user_index(srcUsers,username):
    if srcUsers:
        index = 0
        for user in get_users():
            if user.get("name") == username:
                break
            index += 1
        return True, index
    else:
        return False

if __name__ == '__main__':
    username = 'wd'
    password = 'wd'
    print validate_login(username, password)