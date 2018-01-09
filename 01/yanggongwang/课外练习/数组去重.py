# -*- coding: utf-8 -*-

# 作者：杨公旺
# 日志：2017-11-30
# 功能：数组去重

arr = [1,2,3,4,212,13,14,3,2,12,13,14,3,21,2,2,2,45,22]

new_arr =[]

# 方法1：
#      思路：使用in判断指定值是否存在
#      实现：新建一个数组，存储去重后的数据。如果新数组中不存在指定值，则使用append()函数添加到数组中，否则不添加。
for i in range(0,len(arr)):
    if not arr[i] in new_arr:
        new_arr.append(arr[i])
print new_arr


# 方法2：
#      思路：使用count()统计元素的数量，大于1的元素进行弹出
#      实现：需要循环检测，直到所有元素的计数都是1为止。
for i in arr:
    while True:    
        if arr.count(i)>1:
            arr.remove(i)
        else:
            break
print arr
