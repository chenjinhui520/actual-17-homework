#!/usr/bin/env python
# encoding: utf-8
'''
@author: leiweijie
Create on2017年12月11日
'''
'''
日志分析top
思路：
1、将文件打开读取并装入列表中，使用open()和readlines()
2、使用split()对每一行进行分割，得到ip,url,status
3、使用items()转化成列表
4、冒泡排序（由于时间复杂度高，根据需求只要求top10所以排10次即可）
5、将最后10个插入新列表top10
'''
my_dict = {}
my_list = []
top_10 = []
ngix_log = open('access.txt')
lines = ngix_log.readlines()
for i in lines:
    line = i.split()
    ip = line[0]
    url = line[6]
    status = line[8]
    my_dict[(ip,url,status)] = my_dict.get((ip,url,status),0)+1
#将字典转换成列表
my_list = my_dict.items()
#使用冒泡排序法  由于只需要top10所以只进行最大的10个数排序
for x in range(10):
    for y in range(len(my_list)-x-1):
        if my_list[y][1] > my_list[y+1][1]:
            my_list[y],my_list[y+1] = my_list[y+1],my_list[y]
#取出top10添加到新列表中
for m in range(-1,-11,-1):
    top_10.append(my_list[m])
print top_10   
ngix_log.close()