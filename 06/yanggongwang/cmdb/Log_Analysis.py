# encoding: utf-8

import gconf
import json
import MySQLdb as mysql
from dbutils import execute_sql



# 定义函数
def GetTopN(log_file,topN=10):
    # 第一步：打开文件，统计IP,URL,status获取访问次数
    rt_dict = {}
    log_files = open(log_file, 'r')
    while True:
        line = log_files.readline()
        if not line:
            break
        (ip,url,status) = line.split()[0],line.split()[6],line.split()[8]
        rt_dict[(ip, url, status)] = rt_dict.get((ip, url, status), 0)+1
    log_files.close()
    # 字典数据转换成list，方便排序
    rt_list = rt_dict.items()
    result = sorted(rt_list, key=lambda x: x[1], reverse=True)[:topN]
    return result

if __name__=='__main__':
    log_file = 'access.txt'
    my_list = GetTopN(log_file, topN=3000)
    for i in my_list:
        IP = i[0][0]
        URL = i[0][1]
        my_status = i[0][2]
        my_count = i[1]
        # print IP,URL,my_status,my_count

        sql = 'insert into accesslog(ip,URL,status,count) values(%s,%s,%s,%s)'
        args = (IP,URL,my_status,my_count)
        execute_sql(sql,args=args,fetch=False)


