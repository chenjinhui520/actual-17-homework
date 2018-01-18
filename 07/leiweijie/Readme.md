# 第七次作业
### 用户
1. 实现用户的增、删、改、查
### 日志
1. 实现用户查询查询topn
2. 实现用户上传日志入库并展示




















































CREATE TABLE accesslog (
id int PRIMARY KEY AUTO_INCREMENT,
ip varchar(25),
url text,
status int,
count int
)DEFAULT CHARACTER SET=utf8;


session:
服务器端的存储，
比喻：相当于银行，开户，每个卡号都可以设置过期时间；

cookie：
客户端（浏览器）存储，
比喻：拿到银行卡后，放到家里，session id，



database --> table -->data


插入数据：
insert into tablename(...) values(...)

insert into user(username,password,job,age) values('nick1','123456','cso',27);
insert into user(username,password,job,age) values('nick2','123456','cho',28);
insert into user(username,password,job,age) values('nick3','123456','cio',29);
insert into user(username,password,job,age) values('nick4','123456','cxo',26);


查询数据：
select * from user;
select username,password from user;
# 条件查询
select * from user where username='nick3' and password='123456';
select * from user where age >=27;
select username from user where username='nick4';
select * from user limit 2

删除数据：
delete from user;
delete from user where username='nick';

更新数据：
update user set age=32 where id=4;

md5加密：
update user set password=md5('123456') where id=5;







Python操作MySQL
yum install mysql-devel
pip install MySQL-python
pip list|grep MySQL



# 导入模块
import MySQLdb as mysql
# 创建连接
conn = mysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='cmdb',charset='utf8')
# 获取游标
cur = conn.cursor()

# 插入一条用户数据
//conn.autocommit(True)
cxt = cur.execute("insert into user(username,password,job,age) values('nick6','123456','cxo',25)")
conn.commit()


# 查询数据：
cxt = cur.execute("select * from user")
cur.fetchone()
cur.fetchall()

# 关闭游标和连接
cur.close()
conn.close()


python操作数据库流程
1、导入库
2、创建连接
3、获取游标
4、设置自动提交SQL（可以省略）
5、执行SQL
    a、查询：fetchone/fetchall
    b、写入：commit
6、关闭游标、关闭连接。


("id","username","password","job,age") (2L, u'nick1', u'123456', u'cso', 32L)




