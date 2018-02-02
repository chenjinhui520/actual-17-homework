#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/15日19点11分
import dbutils


# 获取用户列表信息，返回如下格式：
"""
[{'username': u'nick', 'age': 23L, 'job': u'\u8fd0\u7ef4', 'password': u'123123', 'id': 1L}, 
 {'username': u'tanshuai', 'age': 25L, 'job': u'\u74e6\u5de5', 'password': u'123123', 'id': 2L}, 
  {'username': u'wd', 'age': 29L, 'job': u'cto', 'password': u'123123', 'id': 3L}]
"""
def get_users():
    columns = ('id','username','password','job','age')
    sql = 'select * from user'
    rt = []
    count, rt_list = dbutils.execute_sql(sql)
    for line in rt_list:
        rt.append(dict(zip(columns,line)))
    return rt


# 获取单个用户信息
def get_user(uid):
    rt_list = get_users()
    rt_dict = None
    for user in rt_list:
        if int(user.get('id')) == int(uid):
            rt_dict = user
    return rt_dict


# 验证用户名和密码是否重复
def validate_login(username, password):
    args = (username,password)
    sql = 'select * from user where username=%s and password=md5(%s)'
    count, rt_list = dbutils.execute_sql(sql, args)
    return count != 0


# 验证用户名是否重复
def validate_find(username):
    sql = 'select username from user where username=%s'
    count, rt_list = dbutils.execute_sql(sql,(username,))
    return count != 0

'''检查更新用户信息
返回值：True/False，错误信息
'''
def validate_update_user(uid,age,job):
    if get_user(uid) is None:
        return False,u'用户信息不存在'
    if not str(age).isdigit() or int(age) <=0 or int(age) >100:
        return False,u'年龄必须是0到100的数字'
    if job == '':
        return False,u'职务不能为空'
    return True, ''


'''检查添加用户信息
返回值：True/False，错误信息
'''
def validate_add_user(username,password,age,job):
    if username == '':
        return False,u'用户名不能为空'
    if validate_find(username):
        return False, u'用户名存在，请重新输入'
    # 密码要求长度必须大于等于6
    if len(password) < 6:
        return False,u'密码必须大于等于6位'
    if not str(age).isdigit() or int(age) <=0 or int(age) >100:
        return False,u'年龄必须是0到100的数字'
    if job == '':
        return False,u'职务不能为空'
    return True, ''

'''更新密码时验证管理员信息
返回值：True/False，错误信息
'''
def validate_cherge_user_passwd(uid,user_passwd,manage_name,manage_passwd):
    # 直接调用登录验证，即可验证管理员用户名和密码
    if not validate_login(manage_name,manage_passwd):
        return False,u'管理员密码错误'
    # 获取单个用户，先验证是否有这个用户
    if get_user(uid) is None:
        return False,u'没有此用户'
    # 密码要求长度必须大于等于6
    if len(user_passwd) < 6:
        return False,u'密码必须大于等于6位'
    return True, ''

# 更新用户密码
def cherge_user_passwd(uid,user_passwd):
    sql = 'update user set password=md5(%s) where id=%s'
    args = (user_passwd,uid)
    dbutils.execute_sql(sql, args=args, fetch=False)

# 添加用户信息
def add_users(username, age, password, job):
    sql = 'insert into user(username,password,job,age) values(%s,md5(%s),%s,%s)'
    args = (username,password,job,age)
    count, rt_list = dbutils.execute_sql(sql, args=args, fetch=False)
    return count != 0


# 更新用户信息
def update_users(age, job, uid):
    sql = 'update user set job=%s, age=%s where id=%s'
    args = (job, age, uid)
    count, rt_list = dbutils.execute_sql(sql, args=args, fetch=False)
    return count != 0


# 删除用户信息
def del_users(uid):
    sql = 'delete from user where id=%s'
    args = (uid,)
    count, rt_list = dbutils.execute_sql(sql,args=args, fetch=False)
    return count != 0

if __name__ == '__main__':
    # username = 'wd'
    # password = 'wd'
    # print validate_login(username, password)
    print get_user(1)