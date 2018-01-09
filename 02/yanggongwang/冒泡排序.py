# -*- coding: utf-8 -*-
import random

# 作者：杨公旺
# 日志：2017-12-04
# 功能：冒泡排序
# 说明：使用random生成随机数，以确保参与排序的元素的随机性，同时省去人工录入的痛苦。
#       本程序的去重是在写入到列表前进行的。如果写入后在判断，会增加额外的运算量。
#       每次将随机数写入到list时，先判断是否已经存在于列表中，如果不存在则追加到list的结尾。
#       



my_count = 0
my_list = []
while True:
    if my_count == 10:
        break
    my_number = random.randint(0,1000)
    if not my_number in my_list:
        my_list.append(my_number)
        my_count = my_count +1

#print "原始数据是",my_list
print "原始数据是:",
for i in my_list:
    print i,
print ""
    
# 正序排序
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)-1):
        if my_list[i]<my_list[j]:
            my_list[i],my_list[j] = my_list[j],my_list[i]

#print "正序排序结果如下：",my_list
print "正序排序结果如下:",
for i in my_list:
    print i,
print ""


# 逆序排序
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)-1):
        if my_list[i]>my_list[j]:
            my_list[i],my_list[j] = my_list[j],my_list[i]

#print "逆序排序结果如下：",my_list
print "逆序排序结果如下:",
for i in my_list:
    print i,
print ""
