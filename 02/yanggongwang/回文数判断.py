#encoding=utf-8

# 作者：杨公旺
# 日期：2017-12-01
# 需求：判断用户输入是否是回文数
# 功能说明：
#      ：1、用户可以无限次数地输入。
#      ：2、仅int型数字及quit和exit为有效输入。
#      ：3、输入quit或exit，则结束程序。
# 特殊说明：本程序认为一位数（0-9）的数值是回文数，两位数（10-99）全相同的数值也是回文数。


# 关键点：将输入的数值转为list类型的数据进行处理，并适当判断数值小于100的情形。
     
# 方法1：直接判断
# 思路：借用"二分"的思想，以list的中间位置为分界，比对两边的数值是否对称相等。


# 定义一个空list变量，命名为my_list
my_list = []


# 因涉及多次输入，故设计一个"死循环"用于接收用户的输入。
# 为避免变成真的死循环，必需设计循环强制退出的条件。
# 使用isdigit判断用户输入是否合法
while True:
    my_number = raw_input("请输入一个整数:")
    if my_number == "quit" or my_number == "exit":
        print "程序结束！"
        break
    elif not my_number.isdigit():
        print "仅允许输入整数！请重新输入！"
        continue

    my_list = list(my_number)
    if len(my_list) == 1:
        print "您输入的是%s,%s是回文数"%(my_number,my_number)
    elif len(my_list) >1:
        my_len = int(len(my_list)/2)
        for i in range(0,my_len):
            if my_list[i] == my_list[-i-1]:
                print "您输入的是%s,%s是回文数"%(my_number,my_number)
            else:
                print "您输入的是%s,%s不是回文数"%(my_number,my_number)


# 方法二：对输入内容进行逆序输出，使用for循环依次比对两个列表的值是否完全对应
# 说明：此方法的循环次数偏多，但比较容易理解。
# 思路说明：
#    1、将用户的合法输入转为list类型存储。
#    2、新建另一个list类型的数据，内容与上一步的list数据内容相同，但顺序相反。
#    3、使用循环判断两个list类型的数据是否完全相同。即第i个位置的数值是相同的。
#    4、为了确保所有的内容都相同，使用一个计数器统计相同的字符是否与list长度相等，如果相等则说明完全相同，否则不是完全相同。



my_list_new = []

while True:
    my_number = raw_input("请输入一个整数:")
    if my_number == "quit" or my_number == "exit":
        print "程序结束！"
        break
    elif not my_number.isdigit():
        print "仅允许输入整数！请重新输入！"
        continue

    my_list=list(my_number)
    my_list_new=my_list[-1::-1]
    my_count = 0
    for i in range(0,len(my_list)):
        if my_list[i] == my_list_new[i]:
            my_count= my_count +1

    if my_count == len(my_list):
        print "您输入的是%s,%s是回文数"%(my_number,my_number)
    else:
        print "您输入的是%s,%s不是回文数"%(my_number,my_number)











