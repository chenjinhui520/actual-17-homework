# mysql命令总结
本文档在CentOS 6.9操作系统下，基于yum安装的mysql5.1版本完成。

## 数据库操作
### 指定字符集创建数据库
create database python default character set utf8 collate utf8_general_ci;


```
mysql> create database python default character set utf8 collate utf8_general_ci;
Query OK, 1 row affected (0.00 sec)
```
**说明：**
1. python是我创建的数据库名称，下文会多次使用或出现。
2. 使用utf8字符集。
3. 校验规则使用utf8_general_ci。

### 查看所有数据库
show databases;

```
mysql> show databases;      
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| python             |
+--------------------+
3 rows in set (0.00 sec)
```

### 查看建库语句
show create database python;

```
mysql> show create database python;
+----------+-----------------------------------------------------------------+
| Database | Create Database                                                 |
+----------+-----------------------------------------------------------------+
| python   | CREATE DATABASE `python` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+----------+-----------------------------------------------------------------+
1 row in set (0.00 sec)

```
### 删除数据库
drop database python;

## 用户与权限
### 创建用户并授权
create user 'ygw'@'%' identified by '1234';
grant select,insert,update,delete,create on python.* to ygw;

```
mysql> create user 'ygw'@'%' identified by '1234';
Query OK, 0 rows affected (0.00 sec)

mysql> grant select,insert,update,delete,create on python.* to ygw;
Query OK, 0 rows affected (0.00 sec)
```
**说明：**
1. 字符串‘ygw’是账号名，%表示所有主机，字符串‘1234’是密码。
2. grant授权时使用“python.”表示python数据库，\*表示python数据库的所有表。

### 刷新权限
flush  privileges;

```
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
```
### 查看用户
select host,user from mysql.user;

```
mysql> select host,user from mysql.user;
+-----------+------+
| host      | user |
+-----------+------+
| %         | ygw  |
| 127.0.0.1 | root |
| localhost | root |
+-----------+------+
3 rows in set (0.00 sec)
```
### 查看用户权限
show grants for 'ygw'@'%';

```
mysql> show grants for 'ygw'@'%';
+----------------------------------------------------------------------------------------------------+
| Grants for ygw@%                                                                                   |
+----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'ygw'@'%' IDENTIFIED BY PASSWORD '*A4B6157319038724E3560894F7F932C8886EBFCF' |
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE ON `python`.* TO 'ygw'@'%'                            |
+----------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

```
### 取消insert权限
revoke insert on python.* from 'ygw'@'%';

```
mysql> revoke insert on python.* from 'ygw'@'%';
Query OK, 0 rows affected (0.00 sec)

mysql> show grants for 'ygw'@'%';               
+----------------------------------------------------------------------------------------------------+
| Grants for ygw@%                                                                                   |
+----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'ygw'@'%' IDENTIFIED BY PASSWORD '*A4B6157319038724E3560894F7F932C8886EBFCF' |
| GRANT SELECT, UPDATE, DELETE, CREATE ON `python`.* TO 'ygw'@'%'                                    |
+----------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
```

### 取消所有权限
revoke all on python.* from 'ygw'@'%';

```
mysql> revoke all on python.* from 'ygw'@'%';       
Query OK, 0 rows affected (0.00 sec)

mysql> show grants for 'ygw'@'%';            
+----------------------------------------------------------------------------------------------------+
| Grants for ygw@%                                                                                   |
+----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'ygw'@'%' IDENTIFIED BY PASSWORD '*A4B6157319038724E3560894F7F932C8886EBFCF' |
+----------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

```
### 授权与创建用户一条命令搞定
grant all privileges on python.* TO 'ygw'@'127.0.0.1';
grant all privileges on python.* TO 'ygw'@'192.168.1.1';
grant all privileges on python.* TO 'ygw'@'192.168.1.2';

```
mysql> grant all privileges on python.* TO 'ygw'@'127.0.0.1';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all privileges on python.* TO 'ygw'@'192.168.1.1';
Query OK, 0 rows affected (0.00 sec)

mysql> grant all privileges on python.* TO 'ygw'@'192.168.1.2';
Query OK, 0 rows affected (0.00 sec)

mysql> select host,user from mysql.user;
+-------------+------+
| host        | user |
+-------------+------+
| %           | ygw  |
| 127.0.0.1   | root |
| 127.0.0.1   | ygw  |
| 192.168.1.1 | ygw  |
| 192.168.1.2 | ygw  |
| localhost   | root |
+-------------+------+
6 rows in set (0.00 sec)
```
**说明：**
1. grant授权时的all表示所有权限。

### 删除用户
delete from mysql.user where user='ygw' and host='127.0.0.1';  

```
mysql> delete from mysql.user where user='ygw' and host='127.0.0.1';  
Query OK, 1 row affected (0.00 sec)

mysql> select host,user from mysql.user;                            
+-------------+------+
| host        | user |
+-------------+------+
| %           | ygw  |
| 127.0.0.1   | root |
| 192.168.1.1 | ygw  |
| 192.168.1.2 | ygw  |
| localhost   | root |
+-------------+------+
5 rows in set (0.00 sec)

```
use mysql;
drop user 'ygw'@'192.168.1.1';

```
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> drop user 'ygw'@'192.168.1.1';
Query OK, 0 rows affected (0.00 sec)
mysql> select host,user from mysql.user;
+-------------+------+
| host        | user |
+-------------+------+
| %           | ygw  |
| 127.0.0.1   | root |
| 192.168.1.2 | ygw  |
| localhost   | root |
+-------------+------+
4 rows in set (0.00 sec)
```
### 修改密码

```
mysql> update mysql.user set password=PASSWORD("1234")where user="root" and host='127.0.0.1';       
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)


```
## 表操作
### 建表
| 列名 | 类型 | 长度 | 备注 | 是否可空 | 主键 |
| --- | --- | --- | --- | --- | --- |
| id | int | 12 | 用户id | 否 | 是 |
| name | varchar | 64 | 用户名 | 否 | 否 |
| passwd | varchar | 64 | 密码 | 否 | 否 |
| job | varchar | 64 | 职务 | 是 | 否 |
| age | int | 11 | 年龄 | 是 | 否 |
| status | int | 11 | 账号状态，1为禁用，0为启用 | 否 | 否 |
| flag | int | 11 | 连续登录的失败次数 | 是 | 否 |


CREATE TABLE `users` (
	`id` int(12) NOT NULL AUTO_INCREMENT COMMENT '用户id',
	`name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
	`passwd` varchar(64) NOT NULL COMMENT '密码',
	`job` varchar(64) NULL COMMENT '职务',
	`age` int(11) NULL COMMENT '年龄',
	`status` int(11) NOT NULL COMMENT '账号状态，1为禁用，0为启用',
	`flag` int(11) NULL DEFAULT 0 COMMENT '连续登录的失败次数',
	PRIMARY KEY (`id`)
) ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci;


```
mysql> CREATE TABLE `users` (
    -> `id` int(12) NOT NULL AUTO_INCREMENT COMMENT '用户id',
    -> `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
    -> `passwd` varchar(64) NOT NULL COMMENT '密码',
    -> `job` varchar(64) NULL COMMENT '职务',
    -> `age` int(11) NULL COMMENT '年龄',
    -> `status` int(11) NOT NULL COMMENT '账号状态，1为禁用，0为启用',
    -> `flag` int(11) NULL DEFAULT 0 COMMENT '连续登录的失败次数',
    -> PRIMARY KEY (`id`)
    -> ) ENGINE=InnoDB
    -> DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci;
Query OK, 0 rows affected (0.01 sec)
```
**说明：**
1. id字段递增，主键。
2. COMMENT后面的字符串是注释内容
3. DEFAULT用于设置该字段的默认值。
4. 表名users后面会多次使用、出现。

### 查看建表语句
show CREATE TABLE users;

```
mysql> show CREATE TABLE `users`;
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(12) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `name` varchar(64) NOT NULL DEFAULT '' COMMENT '用户名',
  `passwd` varchar(64) NOT NULL COMMENT '密码',
  `job` varchar(64) DEFAULT NULL COMMENT '职务',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `status` int(11) NOT NULL COMMENT '账号状态，1为禁用，0为启用',
  `flag` int(11) DEFAULT '0' COMMENT '连续登录的失败次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```
### 查看表的所有字段（为了查看注释）
show full fields from users; 


```
mysql> show full fields from users;  
+--------+-------------+-----------------+------+-----+---------+----------------+---------------------------------+---------------------------------------------------+
| Field  | Type        | Collation       | Null | Key | Default | Extra          | Privileges                      | Comment                                           |
+--------+-------------+-----------------+------+-----+---------+----------------+---------------------------------+---------------------------------------------------+
| id     | int(12)     | NULL            | NO   | PRI | NULL    | auto_increment | select,insert,update,references | 用户id                                          |
| name   | varchar(64) | utf8_general_ci | NO   |     |         |                | select,insert,update,references | 用户名                                         |
| passwd | varchar(64) | utf8_general_ci | NO   |     | NULL    |                | select,insert,update,references | 密码                                            |
| gid    | int(11)     | NULL            | NO   |     | 1       |                | select,insert,update,references | 用户组ID，0是管理组，1是普通用户组 |
| job    | varchar(64) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references | 职务                                            |
| age    | int(11)     | NULL            | YES  |     | NULL    |                | select,insert,update,references | 年龄                                            |
| status | int(11)     | NULL            | NO   |     | NULL    |                | select,insert,update,references | 账号状态，1为禁用，0为启用            |
| flag   | int(11)     | NULL            | YES  |     | 0       |                | select,insert,update,references | 连续登录的失败次数                       |
+--------+-------------+-----------------+------+-----+---------+----------------+---------------------------------+---------------------------------------------------+
8 rows in set (0.00 sec)

```

### 查看所有表名
show tables;
```
mysql> show tables;
+------------------+
| Tables_in_python |
+------------------+
| users            |
+------------------+
1 row in set (0.00 sec)
```
### 查看表结构
desc users;

```
mysql> desc users;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(12)     | NO   | PRI | NULL    | auto_increment |
| name   | varchar(64) | NO   |     |         |                |
| passwd | varchar(64) | NO   |     | NULL    |                |
| job    | varchar(64) | YES  |     | NULL    |                |
| age    | int(11)     | YES  |     | NULL    |                |
| status | int(11)     | NO   |     | NULL    |                |
| flag   | int(11)     | YES  |     | 0       |                |
+--------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)
```
### 修改表结构（增加字段）
alter table users add birth date not null default '0000-00-00';

alter table users add gid int not null default 1 comment '用户组ID，0是管理组，1是普通用户组' after passwd;


```
mysql> alter table users add birth date not null default '0000-00-00';
Query OK, 1 row affected (0.02 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> desc users;
+--------+-------------+------+-----+------------+----------------+
| Field  | Type        | Null | Key | Default    | Extra          |
+--------+-------------+------+-----+------------+----------------+
| id     | int(12)     | NO   | PRI | NULL       | auto_increment |
| name   | varchar(64) | NO   |     |            |                |
| passwd | varchar(64) | NO   |     | NULL       |                |
| job    | varchar(64) | YES  |     | NULL       |                |
| age    | int(11)     | YES  |     | NULL       |                |
| status | int(11)     | NO   |     | NULL       |                |
| flag   | int(11)     | YES  |     | 0          |                |
| birth  | date        | NO   |     | 0000-00-00 |                |
+--------+-------------+------+-----+------------+----------------+
8 rows in set (0.00 sec)

mysql> alter table users add gid int not null default 1 comment '用户组ID，0是管理组，1是普通用户组' after passwd;
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> desc users;
+--------+-------------+------+-----+------------+----------------+
| Field  | Type        | Null | Key | Default    | Extra          |
+--------+-------------+------+-----+------------+----------------+
| id     | int(12)     | NO   | PRI | NULL       | auto_increment |
| name   | varchar(64) | NO   |     |            |                |
| passwd | varchar(64) | NO   |     | NULL       |                |
| gid    | int(11)     | NO   |     | 1          |                |
| job    | varchar(64) | YES  |     | NULL       |                |
| age    | int(11)     | YES  |     | NULL       |                |
| status | int(11)     | NO   |     | NULL       |                |
| flag   | int(11)     | YES  |     | 0          |                |
| birth  | date        | NO   |     | 0000-00-00 |                |
+--------+-------------+------+-----+------------+----------------+
9 rows in set (0.00 sec)
```

### 修改表结构（修改字段）
alter table users modify birth int not null default 1 comment '测试修改字段类型等信息';

alter table users change birth birthday int not null default 1 comment '测试修改字段名称'; 


```
mysql> alter table users modify birth int not null default 1 comment '测试修改字段类型等信息';
Query OK, 1 row affected, 1 warning (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 1

mysql> desc users;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(12)     | NO   | PRI | NULL    | auto_increment |
| name   | varchar(64) | NO   |     |         |                |
| passwd | varchar(64) | NO   |     | NULL    |                |
| gid    | int(11)     | NO   |     | 1       |                |
| job    | varchar(64) | YES  |     | NULL    |                |
| age    | int(11)     | YES  |     | NULL    |                |
| status | int(11)     | NO   |     | NULL    |                |
| flag   | int(11)     | YES  |     | 0       |                |
| birth  | int(11)     | NO   |     | 1       |                |
+--------+-------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

mysql> alter table users change birth birthday int not null default 1 comment '测试修改字段名称';      
Query OK, 1 row affected (0.02 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> desc users;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(12)     | NO   | PRI | NULL    | auto_increment |
| name     | varchar(64) | NO   |     |         |                |
| passwd   | varchar(64) | NO   |     | NULL    |                |
| gid      | int(11)     | NO   |     | 1       |                |
| job      | varchar(64) | YES  |     | NULL    |                |
| age      | int(11)     | YES  |     | NULL    |                |
| status   | int(11)     | NO   |     | NULL    |                |
| flag     | int(11)     | YES  |     | 0       |                |
| birthday | int(11)     | NO   |     | 1       |                |
+----------+-------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

```
### 修改表结构（删除字段）
alter table users drop birthday;

```
mysql> alter table users drop birthday;
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> desc users;                     
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(12)     | NO   | PRI | NULL    | auto_increment |
| name   | varchar(64) | NO   |     |         |                |
| passwd | varchar(64) | NO   |     | NULL    |                |
| gid    | int(11)     | NO   |     | 1       |                |
| job    | varchar(64) | YES  |     | NULL    |                |
| age    | int(11)     | YES  |     | NULL    |                |
| status | int(11)     | NO   |     | NULL    |                |
| flag   | int(11)     | YES  |     | 0       |                |
+--------+-------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)


```
### 插入数据
insert into users values(1,'yang','yangpwd','op','12',0,0);
```
mysql> insert into users values(1,'yang','yangpwd','op','12',0,0);
Query OK, 1 row affected (0.00 sec)
```

### 查看所有字段
select * from users;
```
mysql> select * from users;  
+----+------+---------+------+------+--------+------+
| id | name | passwd  | job  | age  | status | flag |
+----+------+---------+------+------+--------+------+
|  1 | yang | yangpwd | op   |   12 |      0 |    0 |
+----+------+---------+------+------+--------+------+
1 row in set (0.00 sec)
```
### 查看指定字段
select name from users; 
select name,job,age from users;    
select * from users where name='yang';


```
mysql> select name from users; 
+------+
| name |
+------+
| yang |
+------+
1 row in set (0.00 sec)

mysql> select name,job,age from users;       
+-------+------+------+
| name  | job  | age  |
+-------+------+------+
| ygw1  | ops  |   12 |
| ygw10 | ops  |   12 |
| ygw01 | ops  |  122 |
| ygw02 | ops  |  122 |
| ygw04 | ops  |  122 |
| ygw   | ops  |  122 |
| wd    | wd   |   12 |
+-------+------+------+
7 rows in set (0.00 sec)

mysql> select * from users where name='yang';
+----+------+---------+------+------+--------+------+
| id | name | passwd  | job  | age  | status | flag |
+----+------+---------+------+------+--------+------+
|  1 | yang | yangpwd | op   |   12 |      0 |    0 |
+----+------+---------+------+------+--------+------+
1 row in set (0.00 sec)

```
### 模糊查找（后补）

```
mysql> select * from user;
+----+----------+----------+------+------+-----+---------------+------------+
| id | username | password | job  | age  | tfa | base32_encode | tfa_status |
+----+----------+----------+------+------+-----+---------------+------------+
|  1 | nick     | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  2 | nick1    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  3 | nick2    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  4 | nick3    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  5 | nick4    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  6 | nick11   | 123      | cxo  |   22 |   0 | NULL          |          0 |
|  7 | ygw      | ygw      | ops  |   22 |   0 | NULL          |          0 |
|  9 | y        | y        | y    |   22 |   0 | NULL          |          0 |
| 10 | y        | y        | y    |   22 |   0 | NULL          |          0 |
| 12 | 123      | 123      | 123  |  123 |   0 | NULL          |          0 |
| 13 | yang     | 1234     | op   |   12 |   0 | NULL          |          1 |
+----+----------+----------+------+------+-----+---------------+------------+
11 rows in set (0.00 sec)

mysql> select * from user where username like 'nick%';
+----+----------+----------+------+------+-----+---------------+------------+
| id | username | password | job  | age  | tfa | base32_encode | tfa_status |
+----+----------+----------+------+------+-----+---------------+------------+
|  1 | nick     | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  2 | nick1    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  3 | nick2    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  4 | nick3    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  5 | nick4    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  6 | nick11   | 123      | cxo  |   22 |   0 | NULL          |          0 |
+----+----------+----------+------+------+-----+---------------+------------+
6 rows in set (0.00 sec)

mysql> select * from user where username like 'nick_';
+----+----------+----------+------+------+-----+---------------+------------+
| id | username | password | job  | age  | tfa | base32_encode | tfa_status |
+----+----------+----------+------+------+-----+---------------+------------+
|  2 | nick1    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  3 | nick2    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  4 | nick3    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  5 | nick4    | 123      | cxo  |   25 |   0 | NULL          |          0 |
+----+----------+----------+------+------+-----+---------------+------------+
4 rows in set (0.00 sec)

```
### 限制返回的查找结果数量（后补）

```
mysql> select * from user where username like 'nick%';
+----+----------+----------+------+------+-----+---------------+------------+
| id | username | password | job  | age  | tfa | base32_encode | tfa_status |
+----+----------+----------+------+------+-----+---------------+------------+
|  1 | nick     | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  2 | nick1    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  3 | nick2    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  4 | nick3    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  5 | nick4    | 123      | cxo  |   25 |   0 | NULL          |          0 |
|  6 | nick11   | 123      | cxo  |   22 |   0 | NULL          |          0 |
+----+----------+----------+------+------+-----+---------------+------------+
6 rows in set (0.00 sec)

mysql> select * from user where username like 'nick%' limit 1; 
+----+----------+----------+------+------+-----+---------------+------------+
| id | username | password | job  | age  | tfa | base32_encode | tfa_status |
+----+----------+----------+------+------+-----+---------------+------------+
|  1 | nick     | 123      | cxo  |   25 |   0 | NULL          |          0 |
+----+----------+----------+------+------+-----+---------------+------------+
1 row in set (0.00 sec)
```

### 插入部分值
insert into users(id,name,passwd,job,age,status) values(2,'ygw','ygw','ops',12,1);

insert into users(name,passwd,job,age,status) values('ygw','ygw','ops',12,1);


```
mysql> insert into users(id,name,passwd,job,age,status) values(2,'ygw','ygw','ops',12,1);
Query OK, 1 row affected (0.00 sec)

mysql> select * from users;
+----+------+---------+-----+------+------+--------+------+
| id | name | passwd  | gid | job  | age  | status | flag |
+----+------+---------+-----+------+------+--------+------+
|  1 | yang | yangpwd |   1 | op   |   12 |      0 |    0 |
|  2 | ygw  | ygw     |   1 | ops  |   12 |      1 |    0 |
+----+------+---------+-----+------+------+--------+------+
2 rows in set (0.00 sec)

mysql> insert into users(name,passwd,job,age,status) values('ygw','ygw','ops',12,1);
Query OK, 1 row affected (0.00 sec)

mysql> select * from users;
+----+------+---------+-----+------+------+--------+------+
| id | name | passwd  | gid | job  | age  | status | flag |
+----+------+---------+-----+------+------+--------+------+
|  1 | yang | yangpwd |   1 | op   |   12 |      0 |    0 |
|  2 | ygw  | ygw     |   1 | ops  |   12 |      1 |    0 |
|  3 | ygw  | ygw     |   1 | ops  |   12 |      1 |    0 |
+----+------+---------+-----+------+------+--------+------+
3 rows in set (0.00 sec)
```
### 修改数据（后补）
update users SET flag=0 where name='ygw05';


```
mysql> select flag from users where name='ygw05';  
+------+
| flag |
+------+
|    7 |
+------+
1 row in set (0.00 sec)

mysql> update users SET flag=0 where name='ygw05';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select flag from users where name='ygw05'; 
+------+
| flag |
+------+
|    0 |
+------+
1 row in set (0.00 sec)
```


### 删除数据
delete from users where name='ygw';

```
mysql> delete from users where name='ygw';
Query OK, 2 rows affected (0.00 sec)

mysql> select * from users;          
+----+------+---------+-----+------+------+--------+------+
| id | name | passwd  | gid | job  | age  | status | flag |
+----+------+---------+-----+------+------+--------+------+
|  1 | yang | yangpwd |   1 | op   |   12 |      0 |    0 |
+----+------+---------+-----+------+------+--------+------+
1 row in set (0.00 sec)

```
### 清空表数据
truncate table users;

```
mysql> select * from users;  
+----+------+---------+-----+------+------+--------+------+
| id | name | passwd  | gid | job  | age  | status | flag |
+----+------+---------+-----+------+------+--------+------+
|  1 | yang | yangpwd |   1 | op   |   12 |      0 |    0 |
+----+------+---------+-----+------+------+--------+------+
1 row in set (0.00 sec)

mysql> truncate table users;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from users; 
Empty set (0.00 sec)
```
### 删除表
drop table my_users;
```
mysql> show tables;
+------------------+
| Tables_in_python |
+------------------+
| my_users         |
| users            |
+------------------+
2 rows in set (0.00 sec)

mysql> drop table my_users;
Query OK, 0 rows affected (0.00 sec)

mysql> show tables;        
+------------------+
| Tables_in_python |
+------------------+
| users            |
+------------------+
1 row in set (0.00 sec)

```
## 索引
### 创建唯一索引（专业术语是啥？）
避免字段值重复
ALTER TABLE `users` ADD UNIQUE KEY `userNmae`(`name`);

```
mysql> ALTER TABLE `users` ADD UNIQUE KEY `userNmae`(`name`);
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0
```
### 查看索引
show  index from users;
show  keys from users;

```
mysql> show  index from users;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| users |          0 | PRIMARY  |            1 | id          | A         |           1 |     NULL | NULL   |      | BTREE      |         |
| users |          0 | userNmae |            1 | name        | A         |           1 |     NULL | NULL   |      | BTREE      |         |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
2 rows in set (0.00 sec)

mysql> show  keys from users;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| users |          0 | PRIMARY  |            1 | id          | A         |           1 |     NULL | NULL   |      | BTREE      |         |
| users |          0 | userNmae |            1 | name        | A         |           1 |     NULL | NULL   |      | BTREE      |         |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
2 rows in set (0.00 sec)

```

### 删除索引
drop index userNmae on users;


```
mysql> drop index userNmae on users;
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> show  keys from users;       
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| users |          0 | PRIMARY  |            1 | id          | A         |           1 |     NULL | NULL   |      | BTREE      |         |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
1 row in set (0.00 sec)
```

### 删除主键索引
ALTER TABLE my_users DROP PRIMARY KEY;


```
mysql> DROP TABLE IF EXISTS my_users;
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE TABLE `my_users` (
    -> `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
    -> `passwd` varchar(64) NOT NULL COMMENT '密码',
    -> `job` varchar(64) NULL COMMENT '职务',
    -> `age` int(11) NULL COMMENT '年龄',
    -> `status` int(11) NOT NULL COMMENT '账号状态，1为禁用，0为启用',
    -> `flag` int(11) NULL DEFAULT 0 COMMENT '连续登录的失败次数',
    -> PRIMARY KEY (`name`),
    -> CONSTRAINT userName UNIQUE (name)
    -> ) ENGINE=InnoDB
    -> DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci;
Query OK, 0 rows affected (0.00 sec)

mysql> show  keys from my_users;    
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| Table    | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| my_users |          0 | PRIMARY  |            1 | name        | A         |           0 |     NULL | NULL   |      | BTREE      |         |
| my_users |          0 | userName |            1 | name        | A         |           0 |     NULL | NULL   |      | BTREE      |         |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
2 rows in set (0.00 sec)

mysql> ALTER TABLE my_users DROP PRIMARY KEY;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show  keys from my_users;             
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| Table    | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
| my_users |          0 | userName |            1 | name        | A         |           0 |     NULL | NULL   |      | BTREE      |         |
+----------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+
1 row in set (0.00 sec)
```
## 重置root密码
重置root密码需要停服，生产环境请慎重操作。

```
[root@python ~]# service mysqld stop
停止 mysqld：                                              [确定]
[root@python ~]# netstat -lntp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address               Foreign Address             State       PID/Program name   
tcp        0      0 0.0.0.0:62113               0.0.0.0:*                   LISTEN      1454/sshd           
tcp        0      0 127.0.0.1:27107             0.0.0.0:*                   LISTEN      2674/mongod         
tcp        0      0 0.0.0.0:80                  0.0.0.0:*                   LISTEN      22456/nginx         
[root@python ~]# mysqld_safe --skip-grant-tables --user=mysql &
[1] 22110
[root@python ~]# 180111 14:21:23 mysqld_safe Logging to '/var/log/mysqld.log'.
180111 14:21:23 mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql

[root@python ~]# netstat -lntp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address               Foreign Address             State       PID/Program name   
tcp        0      0 0.0.0.0:62113               0.0.0.0:*                   LISTEN      1454/sshd           
tcp        0      0 127.0.0.1:27107             0.0.0.0:*                   LISTEN      2674/mongod         
tcp        0      0 0.0.0.0:3306                0.0.0.0:*                   LISTEN      22200/mysqld        
tcp        0      0 0.0.0.0:80                  0.0.0.0:*                   LISTEN      22456/nginx         
[root@python ~]# mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.1.73 Source distribution

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> update mysql.user set password=PASSWORD("newpass")where user="root" and host='localhost';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> mysqladmin -uroot -pnewpass shutdownCtrl-C -- exit!
Aborted
[root@python ~]# mysqladmin -uroot -pnewpass shutdown
180111 14:22:24 mysqld_safe mysqld from pid file /var/run/mysqld/mysqld.pid ended
[1]+  Done                    mysqld_safe --skip-grant-tables --user=mysql
[root@python ~]# netstat -lntp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address               Foreign Address             State       PID/Program name   
tcp        0      0 0.0.0.0:62113               0.0.0.0:*                   LISTEN      1454/sshd           
tcp        0      0 127.0.0.1:27107             0.0.0.0:*                   LISTEN      2674/mongod         
tcp        0      0 0.0.0.0:80                  0.0.0.0:*                   LISTEN      22456/nginx         
[root@python ~]# /etc/init.d/mysqld start
正在启动 mysqld：                                          [确定]
[root@python ~]# mysql -h 127.0.0.1 -uroot -p1234
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
[root@python ~]# mysql -h 127.0.0.1 -uroot -pnewpass
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.1.73 Source distribution

Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| cmdb               |
| mysql              |
| python             |
+--------------------+
4 rows in set (0.00 sec)

mysql> 

```










