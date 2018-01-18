#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/19日21点07分

import MySQLdb as mysql
import gconf


def execute_fetch_sql(sql, args=()):
    conn = None
    cur = None
    count = 0
    rt_list = []
    try:
        conn = mysql.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        cur = conn.cursor()
        count = cur.execute(sql, args)
        rt_list = cur.fetchall()
    except Exception as e:
        print e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return count, rt_list


def execute_commit_sql(sql, args=()):
    conn = None
    cur = None
    count = 0
    try:
        conn = mysql.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        cur = conn.cursor()
        count = cur.execute(sql, args)
        conn.commit()
    except Exception as e:
        print e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return count


# 读写执行sql函数
def execute_sql(sql, args=(), fetch=True):
    conn = None
    cur = None
    count = 0
    rt_list = []
    try:
        conn = mysql.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        cur = conn.cursor()
        count = cur.execute(sql, args)
        if fetch:
            rt_list = cur.fetchall()
        else:
            conn.commit()
    except Exception as e:
        print e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return count, rt_list


# 读写日志
def execute_log_sql(sql, args=(), args_list=[], fetch=True):
    conn = None
    cur = None
    count = 0
    rt_list = []
    try:
        conn = mysql.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT,\
                              user=gconf.MYSQL_USER,passwd=gconf.MYSQL_PASSWD,\
                              db=gconf.MYSQL_DB,charset=gconf.MYSQL_CHARSET)
        cur = conn.cursor()
        if fetch:
            count = cur.execute(sql, args)
            rt_list = cur.fetchall()
        else:
            for args in args_list:
                # args = (args[0][0], args[0][1], args[0][2], args[1])
                # sql,('60.55.42.19', '/data/uploads/avatar/902/middle.jpg', '200', 1)
                # print args
                count = cur.execute(sql, args=(args[0][0], args[0][1], args[0][2], args[1]))
            conn.commit()
    except BaseException as e:
        print e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return count, rt_list
