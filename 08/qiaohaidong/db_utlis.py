# -*- coding:utf8 -*-
import MySQLdb as mysql

from conf.dbconf import HOSTNAME, USERNAME, \
    PASSWORD, CHARSET, DB

# mysql操作模板
# 不适合大数据写入
# 原因是执行一次写入会提交一次，这会导致mysql写入特别慢
def execute_sql(sql, args=(), fetch=True):
    try:
        db = mysql.connect(host=HOSTNAME,
                           user=USERNAME,
                           passwd=PASSWORD,
                           db=DB,
                           charset=CHARSET)
        cursor = db.cursor()
        # count = cursor.execute(sql, args)
        count =  cursor.execute(sql, args)
        if fetch:
            rt_list = cursor.fetchall()
            return count, rt_list
        else:
            db.commit()
    except Exception as err:
        print err
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


# x = execute_sql('select  from users', fetch=True)
# print x
# 查询已存在用户
def fetch_users():
    sql = 'select name from users;'
    count, rt_list = execute_sql(sql, fetch=True)
    return rt_list

# 添加用户
def add_user(username, password, age, job):
    sql = "insert into users(name, password, age, job) values(%s, %s, %s, %s);"
    args = (username, password, age, job)

    execute_sql(sql,  args, fetch=False)

# 修改用户密码
def change_password(username, nepassword):
    sql = "update users set password=%s where name = %s;"
    # 这个不要写反了！！！
    args = (nepassword, username)

    execute_sql(sql, args, fetch=False)

# 查询用户信息
def fetch_information(username):
    sql = "select name, password, age, job from users where name = %s;"
    # args是元组，所以单元素一定要加逗号，否则会当成一个普通字符串处理
    args = (username,)
    key = ('name', 'password', 'age', 'job')

    count, rt_list = execute_sql(sql, args, fetch=True)

    if count == 0:
        raise Exception('Fetch information failed!')
    else:
        user_dict = dict(zip(key, rt_list[0]))
        # return rt_list[0]
        return user_dict


# 用户注销
def log_out(username):
    sql = 'delete from users where name = %s;'
    args = (username,)

    execute_sql(sql, args, fetch=False)

# 修改用户信息，不包含密码
def update_information(username, age, job):
    sql = "update users set age=%s, job=%s where name = %s;"
    args = (age, job, username)

    execute_sql(sql, args, fetch=False)


# 获取所有用户数据
def fetch_all_information():
    sql = 'select name, age, job from users;'
    # 使用args是需要这样的形式，name = %s
    # sql = "select %s, %s, %s from users;"
    # args = ('name', 'age', 'job')

    count, rt_list = execute_sql(sql)

    if count == 0:
        raise Exception('Fetch all information failed!')
    else:
        return rt_list

# 获取指定行数的日志
def fetch_log(line=10):
    sql = 'select * from accesslog limit %s;' % (line)
    count, rt_list = execute_sql(sql)

    if count == 0:
        raise Exception('Fetch all information failed!')
    else:
        return rt_list

change_password('hai', '232323')







