#!/usr/bin/python
# -*- coding:utf-8 -*-

# 作者：杨公旺
# 时间：2017-11-27
# 功能：接收用户输入的姓名和分数，被存储到字典中。
# 说明：
#   1、循环接收输入的用户名和分数。
#   2、用户名只能包含字母和数字。由于目前对正则不太熟，强制设置了该规则。
#   3、分数只能是整数。由于目前对正则不太熟，强制设置了该规则。     
#   4、如果用户名输入不合规，则循环输入用户名。分数输入也遵守该规则。
#   5、用户输入在输入姓名时quit或exit则退出程序程序并打印输入结果。
#   6、如果用户在输入分数时输入quit或exit，则终止程序，不会打印任何结果。
#   7、如果用户输入姓名，但在输入分数时退出程序，则最后一次输入的用户名不写入字典中。
# 不足之处：1、未使用函数；2、对用户的输入校验不太符合实际的生活场景（如姓名规则、分数规则）；3、未能永久保留输入的数据;

# 未解决bug：第一次输入分数不合法，进入循环输入分数阶段。此时如果输入quit或exit，
# 则退回到循环输入用户名阶段，再输入quit或exit时，quit或exit将作为分数值存入字典，直接导致程序的其它部分出错。
# 未避免该bug困扰，将break换成了exit()

my_dict = {}


while True:
    input_name = raw_input("请输入姓名：") 
    if input_name == "quit" or input_name == "exit":
        if len(my_dict) == 0:
            exit()
        else:
            break

    if not str.isalnum(input_name):
        print "姓名只允许包含字母、数字，请检查您的输入，谢谢！"
        continue 
    if input_name in my_dict:
        print "姓名不允许重复，请检查您的输入，谢谢！"
        continue

    while True:
        input_fenshu = raw_input("请重新输入分数：")
        if input_fenshu == "quit" or input_fenshu == "exit":
            exit()
        if not str.isdigit(input_fenshu) or int(input_fenshu)<0 or int(input_fenshu) >100:
            print "分数输入不合规，请核对后后重新输入！"
            continue
        else:
            break

    print input_fenshu
    my_dict[input_name] = input_fenshu

print "记录用户分数的字典如下：%s"%(my_dict)

# 统计平均数
my_sum = 0
avg = 0
j = 0

for i in my_dict:
    print "姓名：%s    分数：%s"%(i,my_dict[i])
    my_sum = my_sum + int(my_dict[i])
    j = j+1
avg = float(my_sum)/j
print "共有%s个人，平均成绩是：%s"%(j,avg)


# 这部分是为了练习将字典中的数据转写到list中，如果不是为了此目的，可以直接将成绩单在写入字典的同时独写入list中
# 统计最大值、最小值
# 将字典中的数据提取并存入list中
arr = []
j = 0
for i in my_dict:
    arr.insert(j,int(my_dict[i]))
    j = j+1

# 对list进行排序。逆序排序。该排序将影响二分法的使用。
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
# 不考虑存在分数相同的情形。如果考虑，则只是增加一些if...else语句而已，当前代码已经太多了，暂时先忽略。
# 最高分、与最低分对应的姓名暂时不实现。思路是：拿着最高（低）分去字典中查找，输入对应的键值对即可。
# 如果最高、最低分数不唯一，则对应的键值对也不唯一，只需将遍历得到的所有键值对输出即可。
print "最高分数是%s  最低分数是%s"%(arr[0],arr[-1])


print "排序后的分数list是%s"%(arr)

# 统计是否大多数人的成绩高于平均值。二分查找list即可。
# 判断人数是奇数个，还是偶数个。针对奇偶分别进行判断
j = len(arr)
mid = int(j/2)
if j%2 == 1:
    if avg >arr[mid]:
        print "大多数人的分数低于平均数！"
    elif avg <arr[mid]:
        print "大多数人的分数高于平均数！"
    else:
        print "这是一个神奇的结果哦！"
else:
    if avg <arr[mid-1] and avg >arr[mid]:
         print "这是一个神奇的结果哦！"
    elif avg <=arr[mid]:
        print "大多数人的分数高于平均数！"
    elif avg >=arr[mid-1]:
        print "大多数人的分数低于平均数！"







