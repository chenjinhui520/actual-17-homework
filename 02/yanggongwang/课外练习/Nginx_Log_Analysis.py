#encoding=utf-8
import os

# 作者：杨公旺
# 日志：2017-12-06
# 功能：统计指定客户端IP的访问情况
# 详细说明：
#       1、使用的日志文件作为参数传入。
#       2、需要统计的IP地址作为参数传入。
#       3、暂时只统计HTTP响应码是200或302的结果。
#       4、假定每条日志对应一次访问。实际环境中，一次访问可能产生多条日志。
#       5、由于nginx日志中body_bytes_sent等参数的值也可能是200或302，统计计数时需要增加限制条件。
# 涉及的技术点：
#       1、字符串分割。使用split()将每一条日志作为一个string按空格分割成多个元素的list。
#       2、文件逐行读取。需要注意换行情况。使用strip('\n')排除空行。



#日志内容示例
#str = 'www.myweb.com 201.19.48.238 0.118 0.078 - [06/Dec/2017:00:00:07 +0800] "GET /api/sync/2 HTTP/1.0" 200 19058 "-" "-" 10.11.120.169 - OK '

# 日志格式
#log_format  access  '$http_host $remote_addr ${request_time} $upstream_response_time '
#                        '- [$time_local] "$request" $status $body_bytes_sent "$http_referer" '
#                        '"$http_user_agent" $server_addr $http_x_forwarded_for $request_completion ';

# i、j、n参数用于统计计数使用
i = 0
j = 0
n = 0

my_input_str = raw_input("请输入要处理的日志文件的完整路径:")
my_input_IP = raw_input("请输入要查询的客户端IP:")

if os.path.exists(my_input_str):
    f = open(my_input_str, "r")
    for line in f.readlines():
        my_str = line.strip('\n')
        my_list = my_str.split()
        if my_input_IP in my_list:
            n += 1
            for my_str in my_list:
                if my_str == "200" and my_list[10] == "200":
                    i +=1
                elif my_str == "302" and my_list[10] == "302":
                    j +=1
    f.close()

print "客户端%s的访问的次数是%s"%(my_input_IP,n)
print "客户端%s的访问结果中响应码是200的次数是%s,响应码是302的次数是%s"%(my_input_IP,i,j)




