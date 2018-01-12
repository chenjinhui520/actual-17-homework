# -*- coding:utf8 -*-
from db_utlis import execute_sql
import MySQLdb as mysql
from conf.dbconf import HOSTNAME, USERNAME, \
    PASSWORD, CHARSET, DB


def handle_logs(log_path):
    count = {}
    data = []

    with open('access.txt', 'r') as f:
        for line in f:
            tmp = line.split(' ')
            ip = tmp[0]
            url = tmp[6]
            status = tmp[8]
            key = (ip, url, status)
            count[key] = count.get(key, 0) + 1

    # 方法1：将dict转换成列表，然后排序

    tmp_list = sorted(count.iteritems(), key=lambda x: x[1], reverse=True)

    try:
        db = mysql.connect(host=HOSTNAME,
                           user=USERNAME,
                           passwd=PASSWORD,
                           db=DB,
                           charset=CHARSET)
        cursor = db.cursor()

        for tmp in tmp_list:
            total, count = tmp
            ip, url, status = total

            sql = "insert into accesslog(ip, url, status, count) values(%s, %s, %s, %s)"
            args = (ip, url, status, count)

            cursor.execute(sql, args)
        db.commit()
    except Exception as err:
        print err
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()



handle_logs('access.txt')