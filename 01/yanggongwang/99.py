#coding=utf-8

# 作者：杨公旺
# 时间：2017-11-27
# 版本：V1.2
# V1.1变更内容：1、输出结果增加空格；2、调整输出结果值i、j的位置顺序。
# V1.2变更内容：1、对输出进行判断，通过增加空格的方式使输出结果对齐。

for i in range(1,10):
    for j in range(1,i+1):
	number=i*j
	if(i==3 and j==3):
	    print " %s * %s = %s    "%(j,i,number),
        elif(i==4 and j==3):
            print " %s * %s = %s    "%(j,i,number),
        else:
            print "%s * %s = %s    "%(j,i,number),
    print " "

