#encoding=utf-8
import gconf
import json
import MySQLdb as mysql
from dbutils import execute_sql
#日志入库
def clear_log_table():
    sql = 'truncate table acc_log'
    count, rt_list = execute_sql(sql, args='', fetch=False)
    return count == 1
def im_log(ip,url,status,count,log_list_id):
    sql = 'insert into acc_log(ip,url,status,count,log_list_id) VALUES (%s,%s,%s,%s,%s)'
    args = (ip,url,status,count,log_list_id)
    count, rt_list = execute_sql(sql, args=args, fetch=False)
    return count != 0
#查询
def query_logs(topn,log_list_id):
    if log_list_id:
        sql = 'select * from acc_log where log_list_id=%s order by count desc limit %s'
        args = (log_list_id,topn)
    else:
        sql = 'select * from acc_log order by count desc limit %s'
        args = (topn, )
    count,rt_list = execute_sql(sql,args)
    return rt_list
#添加上传的日志信息入库
def add_log_list(logname,logpath,counts=0):
    sql = 'insert into log_list(logname,logpath,counts) values(%s,%s,%s)'
    args = (logname,logpath,counts)
    count, rt_list = execute_sql(sql,args=args,fetch=False)
    return count != 0
#add_log_list('access.log','/tmp',counts=0)
def insert_log_count(log_list_id,count):
    sql = 'update log_list set counts=%s where id=%s;'
    args = (count,log_list_id)
    count, rt_list = execute_sql(sql, args=args, fetch=False)
    return count != 0
#获取日志信息表
def get_log_list():
    sql = 'select * from log_list'
    log_list = []
    count, rt_list = execute_sql(sql,fetch=True)
    for id,name,path,counts in rt_list:
        log_list.append({'id':id,'name':name,'path':path,'counts':counts})
    return log_list
def get_log_list_id(log_name):
    sql = 'select id from log_list where logname=%s'
    args =(log_name,)
    count, rt_id = execute_sql(sql,args)
    return rt_id

def del_log(logid):
    sql1 = 'delete from log_list where id=%s'
    sql2 = 'delete from acc_log where log_list_id=%s'
    args=(logid,)
    count, rt_list = execute_sql(sql1, args=args, fetch=False)
    count, rt_list = execute_sql(sql2, args=args, fetch=False)
    return count == 1