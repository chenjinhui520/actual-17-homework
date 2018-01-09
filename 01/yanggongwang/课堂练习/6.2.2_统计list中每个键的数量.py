#!/usr/bin/python
# -*- coding:utf-8 -*-

# 作者：杨公旺
# 日期：2017-11-28
# 功能：统计字典中每个键的数据
# 思路：借用字典类型存储键值对的特性统计每个单词的出现次数，将list中每个单词依次取出并计数。
#       list中的元素作为字典的键，计数作为字典的值。
# 涉及主要功能点：1、遍历取出list的元素；2、字典中新增键值；3、修改字典中指定键的值

list1 = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']

new_list = {}

for i in list1:
    if i in new_list:
        new_list[i] = new_list[i]+1
    else:
        new_list[i] = 1
print new_list 

