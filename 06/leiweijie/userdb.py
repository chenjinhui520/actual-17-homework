# encoding: utf-8

import gconf
import json
from dbutils import execute_sql
import MySQLdb as mysql
def mysql_test(sql):
    conn = mysql.connect(host='192.168.122.1',port=3306,user='root',passwd='root',db='cmdb',charset='utf8')
    cur = conn.cursor()
    cxt = cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# 获取所有用户信息
def get_user():
    columns = ('id','username','password','job','age')
    sql = "select * from user"
    user_list = []
    count,rt_list = execute_sql(sql)
    for user in rt_list:
        user_list.append(dict(zip(columns,user)))
    return user_list 
    
# 登陆时验证用户名和密码
def vilidate_login(username,password):
    
    sql = "select * from user where username=%s and password=md5(%s)" 
    # 预防sql注入 select * from user where username='1' or 1=1;-- and password=md5("");
    args = (username,password)
    count = 0
    count , rt_list = execute_sql(sql, args, fetch=True)
    return count != 0    


def vilidate_find(username,passwd,age,job):
    if not username:
        return True, u'用户名不能为空'
    sql = "select username from user where username=%s"
    args = (username,)
    count ,rt_list= execute_sql(sql, args, fetch=True)
    if count != 0:
        return True, u'用户已存在.'
    if not username:
        return True, u'用户名不能为空'
    if not passwd:
        return True, u'密码不能为空'
    if not age:
        return True, u'年龄不能为空'
    if not job:
        return True, u'职务不能为空'
    return False, ''

def add_user(username,password,age,job):
    sql = "insert into user (username,password,job,age) values (%s,md5(%s),%s,%s)"
    args = (username,password,age,job)
    count ,rt_list = execute_sql(sql, args=args, fetch=False)
    return count !=0


def user_delete(uid):
    sql = 'delete from user where id =%s'
    args = (uid,)
    count , rt_list= execute_sql(sql, args, fetch=False)
    return count != 0    


def get_user_by_name(username):
    srcUser = get_user()
    rt_dict = {}
    for user in srcUser:
        if user.get("name") == username:
            rt_dict = user
    return rt_dict

def get_user_by_id(uid):
    columns = ("id","username","password","job","age")
    sql = "select * from user where id = %s"
    args = (uid,)
    user_list = []
    count, rt_list = execute_sql(sql, args, fetch=True)
    for user in rt_list:
        user_list.append(dict(zip(columns,user)))
    return user_list
def user_update(uid,age,job):
    sql = 'update user set job=%s,age=%s where id =%s'
    args = (job,age,uid)
    count , rt_list= execute_sql(sql, args, fetch=False)
    return count != 0


if __name__=='__main__':
    # print get_user()
#     _user= get_user_by_id(3)[0]
    print user_update(1,'1111', 'work1111')