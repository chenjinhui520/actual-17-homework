#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/11/19日21点07分

import MySQLdb as mysql
import gconf


class MySQLConnection(object):
    def __init__(self,host,port,user,passwd,db,charset='utf-8'):
        '''这些属性没必要在外面调用，所以设置成私有属性'''
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset
        self.__conn = None
        self.__cur = None
        self.__connect()

    def __connect(self):
        '''连接数据库有可能会异常，使用try获取异常'''
        try:
            self.__conn = mysql.connect(host=self.__host,port=self.__port,\
                          user=self.__user,passwd=self.__passwd,\
                          db=self.__db,charset=self.__charset)
            self.__cur = self.__conn.cursor()
        except BaseException as e:
            # import traceback
            # print traceback.format_exc()
            print e

    def execute(self,sql,args=()):
        '''执行之前，一定要判断有游标，才能执行, 返回执行后影响的行数'''
        count = 0
        if self.__cur:
            count = self.__cur.execute(sql, args)
        return count

    def fetch(self,sql,args=()):
        '''查询函数接收sql及args传参，通过前面定义的execute方法执行后，使用fetchall查询数据库结果'''
        count = 0
        rt_list = []
        if self.__cur:
            count = self.execute(sql,args)
            rt_list = self.__cur.fetchall()
        return count, rt_list

    def commit(self):
        '''提交请求的时候，需要判断conn连接是否存在，存在才能commit'''
        if self.__conn:
            self.__conn.commit()

    def close(self):
        '''没有打开的话，关闭是有问题的，所以需要判断一下'''
        # 在关闭之前，调用commit方法提交；
        self.commit()
        if self.__conn:
            self.__conn.close()
            # 关闭之后，恢复None初始值
            self.__conn = None
        if self.__cur:
            self.__cur.close()
            self.__cur = None


    # 读写执行sql函数
    @classmethod
    def execute_sql(cls, sql, args=(), fetch=True):
        count = 0
        rt_list = []
        conn = MySQLConnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        if fetch:
            count, rt_list = conn.fetch(sql, args)
        else:
            count = conn.execute(sql, args)
        conn.close()
        return count, rt_list

    # 读写日志
    @classmethod
    def execute_log_sql(cls, sql, args=(), args_list=[], fetch=True):
        count = 0
        rt_list = []
        conn = MySQLConnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                               user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                               db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        if fetch:
            count, rt_list = conn.fetch(sql, args)
        else:
            for args in args_list:
                count = conn.execute(sql, args=(args[0][0], args[0][1], args[0][2], args[1]))
        conn.close()
        return count, rt_list

if __name__ == '__main__':
    # # 测试写数据
    # sql = 'insert into user(username,password,job,age) values(%s,md5(%s),%s,%s)'
    # args = ('test2_insert','123123','dev',22)
    # count, rt_list = MySQLConnection.execute_sql(sql, args, fetch=False)
    # print count
    # 测试读数据
    sql = 'select * from user'
    count, rt_list = MySQLConnection.execute_sql(sql, fetch=True)
    print count,rt_list
