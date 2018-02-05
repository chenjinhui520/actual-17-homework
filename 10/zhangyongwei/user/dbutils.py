# encoding: utf-8
import MySQLdb as mysql
import gconf

def execute_sql(sql,args=(),fetch=True):
    conn = None
    cur = None
    count = 0
    rt_list = []
    try:
        conn = mysql.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT,
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD,
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        cur = conn.cursor()
        count = cur.execute(sql, args)
        if fetch:
            rt_list = cur.fetchall()
        else:
            conn.commit()
    except Exception as e:
        print e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return count,rt_list


class MySQLconnection(object):
    # 定义初始化属性函数
    def __init__(self,host,port,user,passwd,db,charset='utf8'):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset
        self.conn = None
        self.cur = None
        self.connect()

    # 定义方法
    def connect(self):
        try:
            self.conn = mysql.connect(host=self.__host, port=self.__port,
                                      user=self.__user, passwd=self.__passwd,
                                      db=self.__db, charset=self.__charset)
            self.cur = self.conn.cursor()
        except Exception as e:
            print e

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def excute(self,sql,args=(),fetch=True):
        count = 0
        rt_list = []
        if self.cur:
            count = self.cur.execute(sql,args)

        if fetch:
            rt_list = self.cur.fetchall()
        else:
            self.commit()
        self.close()
        return count,rt_list

    @classmethod
    def execute_sql(cls,sql,args=(),fetch=True):
        conn = MySQLconnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT,
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD,
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        count, rt_list = conn.excute(sql, args, fetch)
        return count,rt_list

    @staticmethod
    def execute_sql1(sql,args=(),fetch=True):
        conn = MySQLconnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT,
                             user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD,
                             db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        count, rt_list = conn.excute(sql, args, fetch)
        return count,rt_list

    def __testPrivate(self):
        print 'this is private test'

if __name__ == '__main__':
        # conn = MySQLconnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT,
        #                      user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD,
        #                      db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
        sql = 'select * from user'
        # sql = 'insert into user(username,password,job,age) values("233","2223","22",22)'
        # if conn.conn is None:
        #     print '数据库连接失败'
        # else:
        #     print conn.excute(sql,fetch=False)

        print MySQLconnection.execute_sql(sql)
        # print MySQLconnection.execute_sql(sql,fetch=False)