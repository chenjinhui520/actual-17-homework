#encoding=utf-8
import gconf
import json
import MySQLdb as mysql
from dbutils import execute_sql

#日志入库
def import_log(ip,url,status,count):
    sql = 'insert into acc_log(ip,url,status,count) VALUES (%s,%s,%s,%4)'
    args = (ip,url,status,count)
    count, rt_list = execute_sql(sql, args=args, fetch=False)
    return count != 0
#查询
def query_logs(topn):
    sql = 'select * from acc_log order by count desc limit %s'
    args = (topn,)
    count,rt_list = execute_sql(sql,args)
    return rt_list
