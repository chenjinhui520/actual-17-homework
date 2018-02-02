# encoding: utf-8
from dbutils import execute_sql

'''返回所有资产信息
返回值：[{'id':1,'hostname':'centos7'},{},{}]
'''
def get_list():
    column = ('id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status')
    columns = column.split(',')
    sql = 'select * from assets where status = 0'
    count, rt_list = execute_sql(sql,fetch=True)
    asset_list = [dict(zip(columns,asset)) for asset in rt_list]
    return asset_list

def get_idc():
    sql = 'select id,name from idcs where status = 0'
    count, rt_list = execute_sql(sql,fetch=True)
    return rt_list


'''通过ID标识符，查询IDC机房信息
'''
def get_by_id(aid):
    return None


'''在创建资产时验证输入的信息
返回值：True/False, 错误信息
'''
def vilidate_create_asset(asset_dict):
    assets = get_list()
    if asset_dict.get('_sn').strip().count(' ') !=0:
        return False, '资产编号不能有空格'
    elif asset_dict.get('_sn') == '':
        return False, '资产标号不能为空'
    for asset in assets:
        if asset_dict.get('_sn') == asset.get('sn'):
            return False, '资产编号已存在'
    if asset_dict.get('_purchase_date') == '':
        return False, '请填写采购时间'
    if asset_dict.get('_warranty') == '':
        return False, '请填写保修时长'
    return True, ''


'''创建资产,操作数据库
返回值：True/False
'''
def create_asset(asset_dict):
    sql = 'insert into assets(sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    args_list = []
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
    for i in lists:
        args_list.append(asset_dict.get('_'+i))
    count, rt_list = execute_sql(sql,args=args_list,fetch=False)
    if count != 0:
        return True,'资产添加成功'
    else:
        return False,'资产添加失败'


'''在更新资产时验证输入的信息
返回值：True/False, 错误信息
'''
def vilidate_update_asset(asset_dict):
    if asset_dict.get('__purchase_date') == '':
        return False, '请填写采购时间'
    if asset_dict.get('__warranty') == '':
        return False, '请填写保修时长'
    return True, ''


'''更新资产,操作数据库
返回值：True/False
'''
def update_asset(asset_dict):
    sql = "update assets set ip=%s,hostname=%s,idc_id=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s,admin=%s,business=%s,cpu=%s,ram=%s,disk=%s,os=%s where id=%s"
    args_list = []
    lists = ['ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os','id']
    for i in lists:
        args_list.append(asset_dict.get('__'+i))
    count, rt_list = execute_sql(sql,args=args_list,fetch=False)
    if count != 0:
        return True,'资产更新成功'
    else:
        return False,'资产更新失败'

'''
更新回显
'''
def update_select(aid):
    column = ('id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status')
    columns = column.split(',')
    sql = 'select * from assets where id=%s and status=0'
    args = (aid,)
    count, rt_list = execute_sql(sql,args=args,fetch=True)
    asset_list = [dict(zip(columns,asset)) for asset in rt_list]
    return asset_list

'''删除资产，操作数据库
返回值：True/False
'''
def delete_asset(id):
    sql = 'delete from assets where id=%s'
    args = (id,)
    count, rt_list = execute_sql(sql,args=args,fetch=False)
    return count != 0


if __name__ =='__main__':
    print get_list()