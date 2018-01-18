# encoding: utf-8
from dbutils import execute_sql,executemany_sql

# 定义函数
def GetTopN(log_file='access.txt',topN=10,fetch=True):
    rt_dict = {}
    log_files = open(log_file, 'r')
    while True:
        line = log_files.readline()
        if not line:
            break
        (ip,url,status) = line.split()[0],line.split()[6],line.split()[8]
        rt_dict[(ip, url, status)] = rt_dict.get((ip, url, status), 0)+1
    log_files.close()

    if fetch:
        columns = ("id", "ip", "url", "status", "count")
        sql = 'select * from accesslog limit %s'
        count, rt_list = execute_sql(sql,args=(topN,),fetch=True)
        rt_list = [dict(zip(columns, line)) for line in rt_list]
        return rt_list
    else:
        execute_sql('truncate table accesslog',fetch=False)
        tmp_list = []
        for k,v in rt_dict.items():
            tmp_list.append(list(k)+[v])
        result = sorted(tmp_list, key=lambda x: x[-1], reverse=True)
        sql = 'insert into accesslog(ip,url,status,count) values(%s,%s,%s,%s)'
        count, rt_list = executemany_sql(sql,args=result,fetch=False)
        return count != 0


if __name__=='__main__':
    # 调用函数
    log_file = 'access.txt'
    print GetTopN(log_file,topN=5,fetch=False)