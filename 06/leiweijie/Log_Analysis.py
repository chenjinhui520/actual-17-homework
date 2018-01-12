# encoding: utf-8
from dbutils import execute_sql
from dbutils import executemany_sql

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
    # result = sorted(rt_list, key=lambda x: x[1], reverse=True)[:topN]
    result = sorted(rt_list, key=lambda x: x[1], reverse=True)
    new_list=[]
    for item in result:
        new_list.append((item[0][0],item[0][1],item[0][2],item[1]))
    return new_list

if __name__=='__main__':
    log_file = 'access.txt'
    result = GetTopN(log_file,topN=5)
    sql = "insert into accesslog(ip,url,status,count) values(%s,%s,%s,%s)"
    executemany_sql(sql,args=result,fetch=False)