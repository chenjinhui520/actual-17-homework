#encoding=utf-8
import time

# 作者：杨公旺
# 日期：2017-12-11
# 功能：读取指定nginx日志文件，并根据业务需要进行简单分析
#   统计每个IP对应的状态码的值，并展示Top 10

# 结果展示：
# Top 10的日志内容是:
#     ('123.174.51.164', {'200': 6930, '404': 28})
#     ('111.85.34.165', {'200': 1325, '304': 910, '404': 72})
#     ('118.112.143.148', {'200': 281, '404': 1336})
#     ('117.63.146.40', {'404': 32, '200': 1457})
#     ('118.182.116.39', {'200': 954, '304': 428, '404': 22})
#     ('1.48.219.30', {'200': 1228, '304': 58, '404': 66})
#     ('60.222.231.46', {'200': 1069, '304': 1, '404': 39, '206': 23})
#     ('10.35.1.82', {'200': 1129})
#     ('27.227.163.200', {'200': 833, '304': 41, '404': 69})
#     ('58.253.6.133', {'200': 727, '304': 5, '404': 148})

my_counts = 0
my_list = []
my_dict = {}

f = open('access.txt')

for line in f.readlines():
    nginx_list = line.split()
    client_IP = nginx_list[0]
    nginx_status = nginx_list[8]
    my_dict.setdefault(client_IP, {'total':0}) #为便于Top统计，增加变量total用于统计每个IP访问量
    if client_IP in my_dict:
        if nginx_status in my_dict[client_IP]:
            my_dict[client_IP][nginx_status] += 1
            my_dict[client_IP]['total'] += 1
        else:
            my_dict[client_IP][nginx_status] = 1
            my_dict[client_IP]['total'] += 1
f.close()


# for i in my_dict:
#     my_list.append((i,my_dict[i]))
my_list = my_dict.items()

#只循环10次。每次取出一个"最大值"插入到列表的头部位置
for i in range(10):
    for j in range(i+1,len(my_list)):
        if my_list[i][1]['total'] < my_list[j][1]['total']:
            my_list[i],my_list[j] = my_list[j],my_list[i]


print "Top 10 client IP 访问状态码如下:"
my_new_list = []

for i in range(0,10):
    my_list[i][1].pop('total')  #删除用于计数的临时变量total
    my_new_list.append(my_list[i])

for i in range(0,10):
    print my_new_list[i]

