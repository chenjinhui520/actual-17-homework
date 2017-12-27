# encoding: utf-8

import gconf
import json

# 以list的数据格式返回当前所有的用户名、密码等信息
def get_user():
    with open('users.txt') as f:
        user_list = json.loads(f.read())
    return user_list

# 判断用户名和密码是否匹配，该函数用户登录时的校验
def vilidata_login(username,password):
    user_list = get_user()
    for i in user_list:
        if i.get('name') == username and i.get('passwd') == password:
            return True
    return False

# 检查用户是否存在
# 该函数可以用于用户登录时的校验，即用户名不存在则视为登录失败！
# 该函数用于用户注册、更新信息、删除信息的校验，如果用户名不存在，则运行新增用户；如果用户存在，则运行更新信息或删除用户。
def vilidata_isUser(username):
    user_list = get_user()
    for i in user_list:
        if i.get('name') == username:
            return i.get('name')
    return False

# 检查用户输入的信息是否完整
# 该函数用户校验用户注册时的信息填写是否完整
def check_user_input(**kwargs):
    if kwargs['username'] == '' or kwargs['password1'] == '' or kwargs['password2'] == '':
        return False
    else:
        return True

# 校验两次密码是否相同
# 该函数用于校验用户注册、更新信息时两次输入的密码是否一致
def check_user_password(**kwargs):
    if kwargs['passwd1'] == kwargs['passwd2']:
        return True
    else:
        return False

# 新增用户
# 该函数用于用户注册时数据的持久化
# 函数调用了检查用户名是否存在的函数
# 新增用户成功时返回True，失败时返回False
def add_user(name,passwd,job,age):
    user_dic = {'name':name ,'passwd':passwd,'job':job, 'age':age}
    if not vilidata_isUser(name):
        user_list = get_user()
        user_list.append(user_dic)
        user_list = json.dumps(user_list)
        with open('users.txt', 'w') as f:
            f.writelines(user_list)
        return True
    else:
        return False

# 删除用户
# 该函数用于删除已经存在的用户的所有信息
def del_user(username):
    if vilidata_isUser(username):
        user_list = get_user()  #取出所有用户信息
        for user_info in user_list: #删除指定用户信息
            if user_info['name'] == username:
                user_list.remove(user_info)

        user_list = json.dumps(user_list)
        with open('users.txt', 'w') as f:
            f.writelines(user_list)
        return True
    else:
        return False

# 修改密码
# 该函数用于修改用户信息的密码字段
def change_password(username,password):
    if vilidata_isUser(username):
        user_list = get_user()  #取出所有用户信息
        for user_info in user_list: #修改指定用户的密码字段
            if user_info['name'] == username:
                user_info['passwd'] = password
        user_list = json.dumps(user_list)
        with open('users.txt', 'w') as f:
            f.writelines(user_list)
        return True
    else:
        return False

# 禁用用户账号
# 该函数用于设置用户状态标识位的方式禁用用户账号
# 标识位值为1时，表示该账号被禁用
def disable_user(username):
    if vilidata_isUser(username):
        user_list = get_user()  #取出所有用户信息
        for user_info in user_list: #修改指定用户的密码字段
            if user_info['name'] == username:
                user_info['state'] = 1
        user_list = json.dumps(user_list)
        with open('users.txt', 'w') as f:
            f.writelines(user_list)
        return True
    else:
        return False





if __name__ == '__main__':
    disable_user('ygw')

