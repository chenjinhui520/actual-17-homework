#encoding=utf-8

# 作者：杨公旺
# 功能：将输入字符串的首字母进行大小写转换
# 思路：通过ASCII码值进行大小写转换
#   ASCII码十进制数值48-57对应数字0-9
#   ASCII码十进制数值97-122对应小写字母a-z
#   ASCII码十进制数值65-90对应大写字母A-Z
#   小写字母的ASCII码十进制数值比大写字母大32
#   获得字符c的ASCII值：ord('c')
#   计算ASCII码值56对应的字符：chr(56)


my_input_string = raw_input("请输入字符串：")
if ord(my_input_string[0]) >=48 and ord(my_input_string[0])<=57:
    print "您输入的首字符是数字:%s,不适用字母大小写转换！"%(my_input_string[0])
elif ord(my_input_string[0]) >=65 and ord(my_input_string[0])<=90:
    new_string = chr(ord(my_input_string[0]) + 32)
    for i in range(1,len(my_input_string)):
        new_string += my_input_string[i]
    print "您输入的字符串是%s,经过大小写转换后的字符串是%s." % (my_input_string, new_string)
elif ord(my_input_string[0]) >=97 and ord(my_input_string[0])<=122:
    new_string = chr(ord(my_input_string[0]) - 32)
    for i in range(1,len(my_input_string)):
        new_string += my_input_string[i]
    print "您输入的字符串是%s,经过大小写转换后的字符串是%s." % (my_input_string, new_string)
else:
    print "您输入字符串的首字符既不是数字，也不是字母，不适用字母大小写转换！"

