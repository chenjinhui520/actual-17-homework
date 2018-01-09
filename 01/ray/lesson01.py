#/usr/bin/env python
# _*_ coding:utf-8 _*_
# 打印99乘法表
for i in range(1,10):
    for j in range(1,10):
        if j < i:
            print '%s * %s = %s' %(i,j,(i*j)),
        elif j == i:
            print '%s * %s = %s' %(i,j,(i*j))
        else:
            continue

# 找出最大的2个数
# 使用sorted()函数不会改变list序列，只是临时排序，而使用sort()方法的会改变序列
# function 1
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max_1 = sorted(list)[-1]
max_2 = sorted(list)[-2]
print max_1,max_2

# function 2
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max_1 = None
max_2 = None
for x in list :
	if x > max_1:
		max_1 = x
for y in list:
    if y < max_1:
    	if y > max_2:
    		max_2 = y
print max_1,max_2

# function 3 优化2
max_1 = None
max_2 = None
for x in list:
	if x > max_1:
		max_1 = x
	elif x < max_1 and x > max_2:
		max_2 = x
print max_1,max_2
