#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/15日19点11分
import gconf
import json
import MySQLdb as mysql
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
def get_user(username):
    columns = ('id','username','password','job','age')
    sql = 'select * from user where username=%s'
    rt = []
    count, rt_list = dbutils.execute_sql(sql,args=(username,))
    for line in rt_list:
        rt.append(dict(zip(columns,line)))
    return rt


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

# 添加用户信息
def add_users(username, age, password, job):
    sql = 'insert into user(username,password,job,age) values(%s,md5(%s),%s,%s)'
    args = (username,password,job,age)
    count, rt_list = dbutils.execute_sql(sql, args=args, fetch=False)
    return count != 0


# 更新用户信息
def update_users(username, age, password, job, uid):
    sql = 'update user set username=%s,password=md5(%s),job=%s, age=%s where id=%s'
    args = (username, password, job, age, uid)
    count, rt_list = dbutils.execute_sql(sql, args=args, fetch=False)
    return count != 0


# 删除用户信息
def del_users(uid):
    sql = 'delete from user where id=%s'
    args = (uid,)
    count, rt_list = dbutils.execute_sql(sql,args=args, fetch=False)
    return count != 0

if __name__ == '__main__':
    username = 'wd'
    password = 'wd'
    print validate_login(username, password)