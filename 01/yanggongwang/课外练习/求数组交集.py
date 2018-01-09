# -*- coding: utf-8 -*-

# 作者：杨公旺
# 日志：2017-11-30
# 功能：求两个数组去重后的交集

arr1 = [1,2,3,4,212,13,14,3,2,12,13,14,3,21,2,2,2,45,22]
arr2 = [1,2,3,4,212,12,13,100,14,3,21,200,45,22]

# 去重
# 方法2：
#      思路：使用count()统计元素的数量，大于1的元素进行弹出
#      实现：需要循环检测，直到所有元素的计数都是1为止。
for i in arr1:
    while True:    
        if arr1.count(i)>1:
            arr1.remove(i)
        else:
            break
print "arr数组的内容是%s"%(arr1)


for i in arr2:
    while True:
        if arr2.count(i)>1:
            arr2.remove(i)
        else:
            break
print "arr2数组的内容是%s"%(arr2)

#使用in判断元素是否同时存在于两个数组之中



# 将两个数组合并，找出计数大于1的即可
# 需要将计数为1的元素移除,剩下的都是交集中的元素
arr = arr1 + arr2
for i in arr:
    while True:
        if arr.count(i)==1:
            arr.remove(i)
        else:
            break
# 对交集元素去重
for i in arr:
    while True:
        if arr.count(i)>1:
            arr.remove(i)
        else:
            break

print "两个数组的交集元素是%s"%(arr)
