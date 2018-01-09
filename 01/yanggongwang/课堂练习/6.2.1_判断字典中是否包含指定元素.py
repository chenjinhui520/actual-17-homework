#!/usr/bin/python
# -*- coding:utf-8 -*-

# 作者：杨公旺
# 日期：2017-11-28
# 功能：判断字典中是否包含指定元素

#设置字典内容
my_dict = {'age': 26, 'name': 'nick', 'title': 'devops'}

input_string = raw_input("请输入您要查找的内容:")

# 方法1 使用in判断指定元素是否存在于字典中
if input_string in my_dict:
    print "方法1输出：您查找的内容%s在字典中！"%(input_string)
else:
    print "方法1输出：您查找的内容%s不存在！"%(input_string)

# 方法2 使用for循环遍历字典查找指定元素
flag = 0
for i in my_dict:
    if i == input_string:
        my_key = my_dict[i]
        flag = 1
        print "方法2输出：您查找的内容%s在字典中！该键的取值是%s"%(input_string,my_key)
if flag == 0:
    print "方法2输出：您查找的内容%s不存在！"%(input_string)

