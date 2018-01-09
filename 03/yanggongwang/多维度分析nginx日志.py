#encoding=utf-8
import time

# 作者：杨公旺
# 日期：2017-12-11
# 功能：读取指定nginx日志文件，并根据业务需要进行简单分析



my_counts = 0
my_list = []
my_dict = {}

time_start = time.time()

f = open('access.txt')

for line in f.readlines():
    my_counts +=1

    nginx_list = line.split()
    client_IP = nginx_list[0]
    nginx_URL = nginx_list[6]
    nginx_status = nginx_list[8]
    my_dict.setdefault((client_IP,nginx_URL,nginx_status), 0)
    if (client_IP, nginx_URL, nginx_status) in my_dict:
        my_dict[(client_IP, nginx_URL, nginx_status)] += 1

f.close()
time_end=time.time()
print "日记记录共有%s条"%my_counts
print "提取日志到字典耗时",time_end-time_start,'s'

time_start = time.time()
for i in my_dict:
    my_list.append((i,my_dict[i]))

time_end=time.time()
print "字典到列表转换耗时",time_end-time_start,'s'


time_start = time.time()
#只循环10次。每次取出一个"最大值"插入到列表的头部位置
for i in range(10):
    for j in range(i+1,len(my_list)):
        if my_list[i][1] < my_list[j][1]:
            my_list[i],my_list[j] = my_list[j],my_list[i]

time_end=time.time()
print "列表Top 10排序耗时",time_end-time_start,'s'
print "Top 10的日志内容是:"
for i in range(0,10):
    print  my_list[i]

# 统计响应码是4XX的日志
#for i in my_list:
#    if str(i[0][2])[0] == '4':
#        print i

# 统计响应码是5XX的日志
for i in my_list:
    if str(i[0][2])[0] == '5':
       print i
