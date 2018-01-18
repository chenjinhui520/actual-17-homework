# encoding: utf-8

from dbutils import execute_sql

#数据库建表语句
# CREATE TABLE `audit_logs` (
# 	`date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '当前时间',
# 	`filename` varchar(32) CHARACTER SET utf8 NOT NULL COMMENT '日志文件名',
# 	`path` varchar(128) CHARACTER SET utf8 NOT NULL COMMENT '文件路径',
# 	`username` varchar(32) NOT NULL COMMENT '用户名',
# 	PRIMARY KEY (`date`)
# ) ENGINE=InnoDB
# DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci;


# 记录用户上传日志的时间、文件名、文件存储路径、上传使用的账号
def audit_logs(my_filename,my_path,username):
    sql = 'insert into audit_logs(filename,path,username) values(%s,%s,%s)'
    args = (my_filename,my_path,username)
    count, rt_list = execute_sql(sql, args=args, fetch=False)
    return count != 0

# 展示审计日志
def show_audit_logs(limit_number=10):
    sql = 'select * from audit_logs limit %s'
    args = (limit_number,)
    count, rt_list = execute_sql(sql, args=args, fetch=True)
    return rt_list

if __name__ == '__main__':
   print  show_audit_logs(10)