#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbutils
import time
s = time.time()
# print 'start after:', time.time() - s
def log2db(log_files='', topn=10, fetch=True):
    sql = 'insert into accesslog(ip,url,status,count) values(%s,%s,%s,%s)'
    rt_dict = {}
    _rt = []
    if fetch:   # 查询数据
        _columns = ('id', 'ip', 'url', 'status', 'count')
        sql = 'select * from accesslog order by count desc limit %s'
        _count, _rt_list = dbutils.execute_log_sql(sql, args=(topn,), fetch=True)
        for _list in _rt_list:
            _rt.append(dict(zip(_columns, _list)))
        return _rt
    else:       # 写入数据
        try:
            log_files = open(log_files, 'r')
            while True:
                line = log_files.readline()
                if not line:
                    break
                logs = line.split()
                (ip, url, status) = logs[0], logs[6], logs[8]
                if (ip, url, status) not in rt_dict:
                    rt_dict[(ip, url, status)] = 1
                else:
                    rt_dict[(ip, url, status)] += 1
            log_files.close()
            dbutils.execute_sql('truncate table accesslog',fetch=False)
            _count, _rt_list = dbutils.execute_log_sql(sql, args_list=rt_dict.items(), fetch=False)
            return _count != 0
        except:
            return False


if __name__ == "__main__":
    log_files = '../access.txt'
    # print log2db(log_files=log_files, fetch=False) # 写入logs数据
    print log2db(log_files=log_files, topn=8)  # 读取logs数据
# print 'ok:', time.time() - s

# 建库SQL语句
# create table accesslog (
#   id int primary key auto_increment,
# 	ip varchar(128),
# 	url text,
# 	status int,
# 	count int
# )default charset=utf8;