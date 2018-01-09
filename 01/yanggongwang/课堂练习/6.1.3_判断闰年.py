#!/usr/bin/python
# -*- coding:utf-8 -*-

# 作者：杨公旺
# 日期：2017-11-29
# 功能：给定一个任意年份，判断该年份是否是闰年
# 使用说明：输入quit或exit，则推出程序；除了正常的年份数字，请只输入quit或exit，其它情形的输入程序会异常。
#           暂时不处理非法输入导致的异常。

while True:
    year_input = raw_input("请输入年份：")
    if year_input == 'quit' or year_input == 'exit':
        exit()

    year_input = int(year_input)


    if year_input%100 == 0 and year_input%400 ==0:
        print "您输入的年份是%s,该年是闰年！"%(year_input)
        break
    elif year_input%100 != 0 and year_input%4 ==0:
        print "您输入的年份是%s,该年是闰年！"%(year_input)
        break
    else:
        print "您输入的年份是%s,该年不是闰年！请您继续输入，谢谢！"%(year_input)
