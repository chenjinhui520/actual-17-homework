#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/12/18日22点00分
from dbutils import MySQLConnection


# 用户类
class User(object):
    # __init__是一个类的初始化构造函数
    def __init__(self,id,username,password,job,age):
        self.id = id
        self.username = username
        self.password = password
        self.job = job
        self.age = age

    # 验证用户名和密码是否重复
    @classmethod
    def validate_login(cls, username, password):
        args = (username, password)
        sql = 'select * from user where username=%s and password=md5(%s)'
        count, rt_list = MySQLConnection.execute_sql(sql, args)
        return count != 0

    # 获取用户列表
    @classmethod
    def get_list(cls):
        columns = ('id', 'username', 'password', 'job', 'age')
        sql = 'select * from user'
        rt = []
        count, rt_list = MySQLConnection.execute_sql(sql)
        for line in rt_list:
            rt.append(dict(zip(columns, line)))
        return rt
        # return [User(**dict(zip(columns, _list))) for _list in rt_list]


    #####添加用户#####
    # 验证用户名是否重复
    def validate_find(self):
        sql = 'select username from user where username=%s'
        count, rt_list = MySQLConnection.execute_sql(sql, (self.username,))
        return count != 0
    '''检查添加用户信息
    返回值：True/False，错误信息
    '''
    def validate_add_user(self):
        if self.username == '':
            return False, u'用户名不能为空'
        if self.validate_find():
            return False, u'用户名存在，请重新输入'
        # 密码要求长度必须大于等于6
        if len(self.password) < 6:
            return False, u'密码必须大于等于6位'
        if not str(self.age).isdigit() or int(self.age) <= 0 or int(self.age) > 100:
            return False, u'年龄必须是0到100的数字'
        if self.job == '':
            return False, u'职务不能为空'
        return True, ''
    # 添加用户信息
    def save(self):
        sql = 'insert into user(username,password,job,age) values(%s,md5(%s),%s,%s)'
        args = (self.username, self.password, self.job, self.age)
        count, rt_list = MySQLConnection.execute_sql(sql, args=args, fetch=False)
        return count != 0

    '''
        Flask使用User类来添加用户：
        _user = User(id=None,username=username, age=age, password=password,job=job)
        is_ok, error = _user.validate_add_user()
        if is_ok:
            _user.save()
        return json.dumps({'is_ok': is_ok, 'error': error})
    '''

    #####更新用户#####
    # 获取单个用户信息
    @classmethod
    def get_user(cls,uid):
        rt_list = User.get_list()
        rt_dict = None
        for user in rt_list:
            if int(user.get('id')) == int(uid):
                rt_dict = user
        return rt_dict
    '''检查更新用户信息
    返回值：True/False，错误信息
    '''
    def validate_update_user(self):
        if self.get_user(self.id) is None:
            return False, u'用户信息不存在'
        if not str(self.age).isdigit() or int(self.age) <= 0 or int(self.age) > 100:
            return False, u'年龄必须是0到100的数字'
        if self.job == '':
            return False, u'职务不能为空'
        return True, ''
    # 更新用户信息
    def update(self):
        sql = 'update user set job=%s, age=%s where id=%s'
        args = (self.job, self.age, self.id)
        count, rt_list = MySQLConnection.execute_sql(sql, args=args, fetch=False)
        return count != 0

    '''
        # 实例化用户类
        _user = User(id=uid,age=age,job=job,username=None,password=None)
        is_ok, error = _user.validate_update_user()
        if is_ok:
            _user.update()
            flash(u'更新：%s 成功' % user_dict.get('username'))
        return json.dumps({'is_ok': is_ok, 'error': error})
    
    # 更新用户技术点纪要：
    1、get_user设置成cls，保留uid参数位，以备后面有地方会调用
    2、get_user可以通过User.get_list()获取所有用户信息，进行查询单个用户是否存在
    '''

    #####用户更改密码#####
    '''更新密码时验证管理员信息
    返回值：True/False，错误信息
    '''
    @classmethod
    def validate_cherge_user_passwd(cls,uid,user_passwd,manage_name,manage_passwd):
        # 直接调用登录验证，即可验证管理员用户名和密码
        if not User.validate_login(manage_name,manage_passwd):
            return False,u'管理员密码错误'
        # 获取单个用户，先验证是否有这个用户
        if User.get_user(uid) is None:
            return False,u'没有此用户'
        # 密码要求长度必须大于等于6
        if len(user_passwd) < 6:
            return False,u'密码必须大于等于6位'
        return True, ''

    # 更新用户密码
    @classmethod
    def cherge_user_passwd(cls, uid,user_passwd):
        sql = 'update user set password=md5(%s) where id=%s'
        args = (user_passwd,uid)
        MySQLConnection.execute_sql(sql, args=args, fetch=False)

    '''
    # 更新密码调用：
    is_ok, error = User.validate_cherge_user_passwd(uid,user_passwd,session['user']['username'], manage_passwd)
    msg = ''
    if is_ok:
        User.cherge_user_passwd(uid,user_passwd)
        msg = '用户密码更新成功!'
    return json.dumps({'is_ok':is_ok, 'error':error,'msg':msg})
    '''

    # 删除用户信息
    @classmethod
    def del_users(cls,uid):
        sql = 'delete from user where id=%s'
        count, rt_list = MySQLConnection.execute_sql(sql,args=(uid,), fetch=False)
        return count != 0
    '''
    # 删除用户调用：
    if User.del_users(uid):
        flash(u'删除：%s 成功'%username)
        return redirect('/user/list/')
    else:
        return '用户删除失败！'
    '''




# 资产类
class Asset(object):

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_list(cls):
        column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
        columns = column.split(',')
        sql = 'select {column} from assets where status=0'.format(column=column)
        count, rt_list = MySQLConnection.execute_sql(sql, fetch=True)
        return [dict(zip(columns, line)) for line in rt_list]

    @classmethod
    def get_by_id(cls, aid):
        sql = 'select * from idcs where id=%s and status=0'
        _count, _rt_list = MySQLConnection.execute_sql(sql, args=(aid,), fetch=True)
        return _rt_list

    @classmethod
    def get_idc(cls):
        sql = 'select id, name from idcs where status=0'
        count, rt_list = MySQLConnection.execute_sql(sql, fetch=True)
        return rt_list

    ##########添加资产##########
    @classmethod
    def validate_create(cls, asset_dict):
        assets = cls.get_list()
        if asset_dict.get('_sn').strip().count(' ') != 0:
            return False, u'资产编号不能有空格'
        elif asset_dict.get('_sn') == '':
            return False, u'请填写资产编号'
        for asset in assets:
            if asset.get('sn') == asset_dict.get('_sn'):
                return False, u'资产编号已存在'
        if asset_dict.get('_purchase_date') == '':
            return False, u'请选择采购日期'
        if asset_dict.get('_warranty').strip() == '':
            return False, u'请填写保修时间'
        elif not asset_dict.get('_warranty').strip().isdigit():
            return False, u'保修时长必须为整数'
        return True, ''

    @classmethod
    def save(cls, asset_dict):
        sql = 'insert into assets(sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args_list = []
        lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
        for i in lists:
            args_list.append(asset_dict.get('_'+i))
        _count, _rt_list = MySQLConnection.execute_sql(sql, args=args_list, fetch=False)
        return _count != 0


    ##########删除资产##########
    @classmethod
    def delete(cls, asset_id):
        sql = 'update assets set status=1 where id=%s'
        count, rt_list = MySQLConnection.execute_sql(sql, args=(asset_id,), fetch=False)
        return count != 0


    ##########更新资产##########
    @classmethod
    def validate_update(cls, asset_dict):
        if asset_dict.get('_purchase_date') == '':
            return False, u'请选择采购日期'

        if asset_dict.get('_warranty').strip() == '':
            return False, u'请填写保修时间'
        elif not asset_dict.get('_warranty').strip().isdigit():
            return False, u'保修时长必须为整数'
        return True, ''

    @classmethod
    def update(cls, asset_dict):
        sql = 'update assets set ip=%s,hostname=%s,idc_id=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s,admin=%s,business=%s,cpu=%s,ram=%s,disk=%s,os=%s where id=%s'
        args_list = []
        lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os','id']
        for i in lists:
            args_list.append(asset_dict.get('_'+i))
        print sql
        print args_list
        _count, _rt_list = MySQLConnection.execute_sql(sql, args=args_list, fetch=False)
        return _count != 0