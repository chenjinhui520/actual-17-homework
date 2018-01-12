#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbutils

def log2db(log_file, topn=10, fetch=True):
    sql = 'insert into accesslog(ip,url,status,count) values(%s,%s,%s,%s)'
    log_files = open(log_file, 'r')
    rt_dict = {}
    rt = []
    while True:
        line = log_files.readline()
        if not line:
            break
        nodes = line.split()
        (ip,url,status) = nodes[0],nodes[6],nodes[8]
        if (ip,url,status) not in rt_dict:
            rt_dict[(ip,url,status)] = 1
        else:
            rt_dict[(ip,url,status)] += 1
    log_files.close()
    # print rt_dict

    if fetch:
        # 返回一个排序后的列表
        columns = ('id', 'ip', 'url', 'status', 'count')
        sql = 'select * from accesslog limit %s'
        count, rt_list = dbutils.execute_log_sql(sql, args=(topn,))
        for line in rt_list:
            rt.append(dict(zip(columns,line)))
        return rt
    else:
        # 写入数据
        rt_list = rt_dict.items()
        args_list = sorted(rt_list, key=lambda x: x[1], reverse=True)
        # 排序后：[(('118.112.143.148', '/images/cursor_zoom.cur', '404'), 674)]
        # 写到这，再去设计execute_log_sql函数
        count, rt_list = dbutils.execute_log_sql(sql, args_list=args_list, fetch=False)
        return count != 0

if __name__ == '__main__':
    log_file = '../access.txt'
    # 调用函数
    print log2db(log_file=log_file, topn=10)
