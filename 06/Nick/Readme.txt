# 建库
create database user;

# 建表
create table user (
	id int primary key auto_increment,
	username varchar(25),
	password varchar(32),
	age int
)default charset=utf8;

# （增加）插入数据
insert into user(username,password,age) values('nick','123123',22);
insert into user(username,password,age) values('tanshuai','321321',25);
insert into user(username,password,age) values('wd','sdffds',29);
insert into user(username,password,age) values('kk','234sdfr',24);
insert into user(username,password,age) values('xg','153fweg',28);
#insert into user values('tanshuai','123123',23);


# 查询
select * from user;
select username,password from user;
# where条件查询
select * from user where username='nick' and password='123123';
# 模糊匹配查询
select * from user where username like 'tan%';
# 条件匹配查询
select * from user where age>=23;

# 删除
# 指定条件删除
delete from user # 删除全部表数据
delete from user where id=9; # 删除条件内的表数据


# 更新
# 指定条件更新
update user set username = 'tanyanhong' where id=5;

#md5密码
update user set password = md5('abc') where id 5;


# 用户验证语句
select * from user where username = 'tanshuai' and password = md5('abc');


# 查询表结构
desc user;
show create table user;




# python for mysql
# 创建一个连接
conn = mysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='nick', charset='utf8')
# 获取一个游标
cur = conn.cursor()
# 插入一条数据
cur.execute('insert into user(username,password,age) values("nick",md5("123123"), 22)')
# 手动提交数据
conn.commit()
# 开启自动提交数据
conn.autocommit(True)
cur.execute('insert into user(username,password,age) values("tanshuai",md5("123123"), 23)')

# 跳过前面提交的信息
cur.execute('insert into user(username,password,age) values("tanshuai01",md5("123123"), 23)')
conn.rollback()
cur.execute('insert into user(username,password,age) values("tanshuai02",md5("123123"), 23)')
conn.commit()


#查询数据
cur.execute('select * from user;')
# 一行一行读取
cur.fetchone()
# 全部读取
cur.fetchall()


#　关闭连接
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()


python操作数据库流程
1.导入库
2.创建连接
3.设置自动提交
4.执行sql
5.根据sql类型选择commit还是fetch
	更改类型commit
	查询类型fetchall/fetchone
6.关闭cursor，conn


# sql注入
1"or"1"="1"or "1



# mysql统计数据
select url,ip,status, count(*) from accesslog group by url,ip,status;
select url,ip,status, count(*) as count from accesslog group by url,ip,status order by count;
select * from accesslog order by ip desc limit 6;
select * from accesslog order by count desc limit %s
# 统计ip字段出现的次数并显示倒序10行信息
select ip,count(*) as count from accesslog group by ip order by count desc limit 10;
# 统计url字段出现的次数并显示倒序10行信息
select url,count(*) as count from accesslog group by url order by count desc limit 10;

# 作业
1. 修改，删除改成db
2. 修改和删除唯一标识修改为id
3. logs==>入库                    
    url，ip，code，count

create table accesslog (
    id int primary key auto_increment,
	ip varchar(128),
	url text,
	status int,
	count int
)default charset=utf8;