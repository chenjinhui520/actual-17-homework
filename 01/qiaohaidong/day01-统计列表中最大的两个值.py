# -*- coding: utf-8 -*-

L = [1,2,3,2,12,3,1,3,21,22,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]

# 方法1：使用python内置排序函数
result = sorted(L)
# print(result)
print "The biggest two numbers are {0} and {1}".format(result[-1], result[-2])

# 方法2：冒泡排序

tmp = L
length = len(tmp)
for i in range(length):
    for j in range(length-1):
        if tmp[j] >= tmp[j+1]:
            tmp[j], tmp[j+1] = tmp[j+1], tmp[j]


print "The biggest two numbers are {0} and {1}".format(tmp[-1], tmp[-2])