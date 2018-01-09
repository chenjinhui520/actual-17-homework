#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import Counter
from pprint import pprint

# 需求：取nginx的字段ip, url, status并统计这三个字段出现的top10
# 思路：
# 1 读取文件，将每行文件切割取字段
# 2 将字段封装成元组，用字典统计出现次数
# 3 将字典转换成列表进行排序
#

count = {}
data = []

with open('access.txt', 'r') as f:
    for line in f:
        tmp = line.split(' ')
        ip = tmp[0]
        url = tmp[6]
        status = tmp[8]
        key = (ip, url, status)
        count[key] = count.get(key,0) + 1
        # print key
        
		# 方法3用的数据
		# data.append(key)

# 方法1：将dict转换成列表，然后排序

tmp_list = sorted(count.iteritems(), key=lambda x:x[1], reverse=True)

for i in range(10):
    print tmp_list[i]
	
	
'''
# 方法2：直接对字典的value进行排序，反馈key的列表

tmp_dict = sorted(count, key=lambda x: count[x], reverse=True)

for key in tmp_dict[0:10]:
    print '{0}: {1}'.format(key, count[key])


# 方法3：使用python内置方法Counter，直接统计top10

result = Counter(data)
pprint(result.most_common(10))
'''