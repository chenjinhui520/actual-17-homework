# encoding: utf-8

import gconf
import json
import hashlib
import MySQLdb as mysql
from dbutils import execute_sql
from  Log_Analysis import GetTopN
import os, stat



# 登陆时验证用户名和密码
def vilidate_login(username,password):
    sql = 'select * from user where username=%s and password=md5(%s)'
    args = (username,password)
    count, rt_list = execute_sql(sql,args,fetch=True)
    return count != 0


# 获取所有用户信息
def get_user():
    columns = ("id","username","password","job","age")
    sql = 'select * from user'
    user_list = []
    count, rt_list = execute_sql(sql,fetch=True)
    for user in rt_list:
        user_list.append(dict(zip(columns,user)))
    return user_list

# 获取单个用户信息
def get_one_user(id):
    user_list = []
    sql = 'select id from user where id=%s'
    args = (id,)
    count, user_list =  execute_sql(sql, args, fetch=True)
    if count == 1:
        return True
    else:
        return False


def vilidate_find(username,passwd,age,job):
    if not username:
        return True, u'用户名不能为空'
    sql = "select username from user where username=%s"
    args = (username,)
    count, rt_list = execute_sql(sql, args, fetch=True)
    if count != 0:
        return True, u'用户名已存在'
    if not passwd:
        return True, u'密码不能为空'
    if not age:
        return True, u'年龄不能为空'
    if not job:
        return True, u'职务不能为空'
    return False, ''

# 添加用户
def add_user(username,passwd,age,job):
    sql = 'insert into user(username,password,job,age) values(%s,md5(%s),%s,%s)'
    args = (username,passwd,job,age)
    count, rt_list = execute_sql(sql,args=args,fetch=False)
    return count != 0


def user_delete(uid):
    if get_one_user(uid):
        sql = 'delete from user where id = %s'
        args = (uid,)
        execute_sql(sql, args=args, fetch=False)
        return True
    else:
        return False

def get_user_by_id(uid):
    columns = ("id","username","password","job","age")
    sql = 'select * from user where id=%s'
    args = (uid,)
    user_list = []
    count, rt_list = execute_sql(sql,args=args,fetch=True)
    for user in rt_list:
        user_list.append(dict(zip(columns,user)))
    return user_list


def user_update(uid,age,job):
    sql = 'update user set job=%s,age=%s where id=%s;'
    args = (job,age,uid)
    count, rt_list = execute_sql(sql,args=args,fetch=False)
    return count != 0

def change_user_password(uid,old_passwd,new_passwd):
    sql = 'select password from user where id=%s;'
    args = (uid,)
    count, password = execute_sql(sql,args=args,fetch=True)
    if password[0][0] == hashlib.md5(old_passwd).hexdigest():
        sql1 = 'update user set password=md5(%s) where id=%s;'
        args2 = (new_passwd,uid)
        print new_passwd
        if execute_sql(sql1, args=args2, fetch=False):
            return True
        else:
            return False

# 获取日志信息
def get_accesslogs(TopN):
    columns = ("id","username","password","job","age")
    sql = 'select * from accesslog limit %s'
    args = (TopN,)
    user_list = []
    count, logall_list = execute_sql(sql,args,fetch=True)
    return logall_list

# 日志文件上传

def files_upload(files):
    if files:
        files.save('/tmp/%s' %files.filename)
        os.chmod('/tmp/%s' %files.filename, stat.S_IREAD | stat.S_IWRITE)  # 文件权限:600
        if GetTopN('/tmp/%s' %files.filename, fetch=False): #日志写入mysql数据库中
            return True
        else:
            return False
    else:
        return False





if __name__=='__main__':
    logall_list =  get_accesslogs(2)
    for log in logall_list:
        print log[1]
