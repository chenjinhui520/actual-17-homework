# -*- coding:utf8 -*-
# 检查注册的用户名是否已存在
from db_utlis import execute_sql

def UsernameAlreadyExist(username, users):
    for user in users:
        if username  in user:
            raise Exception('{} name already exists'.format(username))

# 检查密码长度是否小于5
def CheckPasswordLen(password):
    if len(password) < 5:
        raise Exception("The password length is at least 5 bits!")

# 二次验证密码
def DoubleCheckPassword(password, repeat_password):
    if password != repeat_password:
        raise Exception("Sorry, passwords do not match!")

# 检查注册用户名 ，年龄，职业是否为空
# 老方法，扩展性差，已不用
# 在写更新用户数据时发现这个函数不适用于update的检测，所以改用了可变变量
def OldCheckInputIsEmpty(username, age, job):
    # return True if username != '' else False
    if not username:
        raise Exception('Username can not be empty!')
    if not age:
        raise Exception('Age can not be empty!')
    if not job:
        raise Exception('Job can not be empty!')

# 检查注册用户名 ，年龄，职业是否为空
def CheckInputIsEmpty(*args):
    for i in args:
        if not i:
            raise Exception('Information can not be empty!')
# 登陆验证模块
def CheckLogin(username, password):
    sql = 'select * from users where name = %s and password = %s'
    args = (username, password)

    count, rt_list = execute_sql(sql, args, fetch=True)

    if count == 0:
        raise Exception("Verification failed!")
    else:
        return True
