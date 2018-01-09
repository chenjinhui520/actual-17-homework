#encoding=utf-8

import sys,time
log_file='access.txt'
f=open(log_file,'r')
tmp_dict={}
time_start=time.time()
for item in f:   #读取文件
    
    tmpfile = item.split()  #分片，提取关键字    
    IP = tmpfile[0]
    URL = tmpfile[6]
    Status = tmpfile[8]
    #统计数据
    tmp_dict[(IP,URL,Status)]=tmp_dict.get((IP,URL,Status),0)+1
f.close()
length=len(tmp_dict)
item_dict=tmp_dict.items()
# 冒泡排序
for j in range(length-1):
    for i in range(length-1-j):

        if item_dict[i][1]>item_dict[i+1][1]:
            item_dict[i],item_dict[i+1] = item_dict[i+1],item_dict[i]
    #判断第10和以后的次数是否相等，如果相等，则继续，不相等就退出
    #比如第10名和第11名出现的次数一样多，则将第11名也列出
    if j >10:
        if  item_dict[i][1] != item_dict[i+1][1]:
            x=item_dict[-j::]
            x.reverse()
            print x
            time_end = time.time()
            print time_end - time_start, "s"
            sys.exit()

###以下是第二种方法，使用Sorted和lamda函数进行排序反转
#tmp_dict={}
##使用open读取文件
#with open(log_file) as f:
#    for line in f:
#        tmpfile = line.split()
#        IP = tmpfile[0]
#        URL = tmpfile[6]
#        Status = tmpfile[8]
#        tmp_dict[(IP,URL,Status)]=tmp_dict.get((IP,URL,Status),0)+1
#
##使用sorted和lamda进行排序，reverse反转
#tmp_list=sorted(tmp_dict.items(),key=lambda d:d[1],reverse=True)
#j=1
#for i in tmp_list:
#    print i
#    if j >10:
#        if tmp_list[j][1] != tmp_list[j+1][1]:
#            time_end = time.time()
#            print time_end - time_start, "s"
#            sys.exit()
#    j+=1
