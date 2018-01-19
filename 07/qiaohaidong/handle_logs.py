# -*- coding:utf8 -*-
import MySQLdb as mysql
from db_utlis import execute_sql
from conf.dbconf import HOSTNAME, USERNAME, \
    PASSWORD, CHARSET, DB
from time import time


def execute_manysql(sql, args=(), fetch=True):
    try:
        db = mysql.connect(host=HOSTNAME,
                           user=USERNAME,
                           passwd=PASSWORD,
                           db=DB,
                           charset=CHARSET)
        cursor = db.cursor()
        # count = cursor.execute(sql, args)
        count =  cursor.executemany(sql, args)
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


def handle_logs(log_path):
    count = {}

    with open(log_path, 'r') as f:
        for line in f:
            tmp = line.split(' ')
            ip = tmp[0]
            url = tmp[6]
            status = tmp[8]
            key = (ip, url, status)
            count[key] = count.get(key, 0) + 1
    # 将字典转换成[ip, url, status, count]的生成器
    args = (list(key) + [value] for key, value in count.items())
    # 对生成器进行排序
    # args = sorted(tmp_list, key=lambda x: x[3], reverse=True)
    # stop1 = time()

    sql =  "insert into accesslog(ip, url, status, count) values(%s, %s, %s, %s)"
    execute_manysql(sql, args, fetch=False)

def fetch_result(line):
    sql = 'select * from accesslog order by count desc limit %s;' % line
    args = ()
    count, rt_list = execute_sql(sql, args, fetch=True)
    return rt_list


print(fetch_result(10))

