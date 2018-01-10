# encoding: utf-8

import gconf
import json

import MySQLdb as mysql
from dbutils import execute_sql



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
    sql = 'delete from user where id=%s' % uid
    count, rt_list = execute_sql(sql,fetch=False)
    return count != 0


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


if __name__=='__main__':
    # print get_user()
    # print vilidate_login('wd','wd')
    # print get_user_by_name('wd')
    # print vilidate_login('nick5','123456')
    # print get_user()
    # print get_user_by_id(17)
    print user_update(17,23,'cto')