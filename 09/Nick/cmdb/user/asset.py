#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/12/6日21点07分
import dbutils

'''返回所有资产信息
返回值：[{'sn': '', 'id': '',...},{},{}]
'''
def get_list():
    column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
    columns = column.split(',')
    sql = 'select {column} from assets where status=0'.format(column=column)
    count, rt_list = dbutils.execute_sql(sql, fetch=True)
    rt = []
    for line in rt_list:
        rt.append(dict(zip(columns, line)))
    return rt
    # return [dict(zip(columns, line)) for line in rt_list]

'''返回所有IDC机房信息
返回值：[]
'''
def get_idc():
    sql = 'select id, name from idcs where status=0'
    count, rt_list = dbutils.execute_sql(sql, fetch=True)
    return rt_list

'''通过ID标识符，查询IDC机房信息
返回值：True/False，IDC机房信息
'''
def get_by_id(aid):
    sql = 'select * from idcs where id=%s and status=0'
    _count, _rt_list = dbutils.execute_sql(sql, args=(aid,), fetch=True)
    return _rt_list

'''在创建资产时对输入信息进行检查
返回值：True/False, error_msg{}
'''
def validate_create(asset_dict):
    assets = get_list()
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


'''创建资产，操作数据库
返回值：True/False
'''
def create(asset_dict):
    sql = 'insert into assets(sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    args_list = []
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
    for i in lists:
        args_list.append(asset_dict.get('_'+i))
    _count, _rt_list = dbutils.execute_sql(sql, args=args_list, fetch=False)
    return _count != 0


'''在更新资产时对输入信息进行验证
返回值：True/False, error_msg{}
'''
def validate_update(asset_dict):
    if asset_dict.get('_purchase_date') == '':
        return False, u'请选择采购日期'

    if asset_dict.get('_warranty').strip() == '':
        return False, u'请填写保修时间'
    elif not asset_dict.get('_warranty').strip().isdigit():
        return False, u'保修时长必须为整数'
    return True, ''


'''更新资产，操作数据库
返回值：True/False
'''
def update(asset_dict):
    sql = 'update assets set ip=%s,hostname=%s,idc_id=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s,admin=%s,business=%s,cpu=%s,ram=%s,disk=%s,os=%s where id=%s'
    args_list = []
    lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os','id']
    for i in lists:
        args_list.append(asset_dict.get('_'+i))
    print sql
    print args_list
    _count, _rt_list = dbutils.execute_sql(sql, args=args_list, fetch=False)
    return _count != 0


'''删除资产，操作数据库
返回值：True/False
'''
def delete(asset_id):
    sql = 'update assets set status=1 where id=%s'
    count, rt_list = dbutils.execute_sql(sql, args=asset_id, fetch=False)
    return count != 0

if __name__ == '__main__':

    # print get_list()
    print get_by_id(2)
