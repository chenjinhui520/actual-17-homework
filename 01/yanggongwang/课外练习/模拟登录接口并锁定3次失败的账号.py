#encoding=utf-8

# 作者：杨公旺
# 日期：2017-12-01
# 需求：模拟一个登录接口，接收用户账号和密码。
#       如果登录成功，则显示欢迎信息。
#       三次登录失败，则锁定该账号。
#   
# 锁定功能的实现：暂时将账号写入到数组中，在验证密码前进行校验
# 思路说明：
#     1、创建一定字典类型的tmp_names变量，用于记录用户登录失败的次数。该计数将在用户成功登录后被重置。
#     2、创建一个list类型的变量lock_names，用于记录被锁定的账号。由于未做持久化存储，在程序执行期间，被锁定的账号不会被解锁。
#     3、登录失败三次的账号将被写入到lock_names变量中.




user_name = "51reboot"
user_password = "51reboot"
lock_names = []
tmp_names = {}

while True:
    print "输入exit或quit结束程序！"

    my_name = raw_input("请输入用户名：")
    if my_name == "exit" or my_name == "quit":
        break

    my_password = raw_input("请输入密码：")
    if my_password == "exit" or my_password == "quit":
        break

    if my_name in lock_names:
        print "该账号已被锁定，如需解锁，请连续管理员！"
        tmp_names[my_name] = str(int(tmp_names[my_name])+1)
    elif "51reboot" == my_name and "51reboot" == my_password:
        print "欢迎您访问！"
        if my_name in tmp_names:
            del tmp_names[my_name]
    else:
        print "你输入的用户名或密码错误！"
        if not my_name in tmp_names:
            tmp_names[my_name] = "1"
        elif int(tmp_names[my_name]) == 1:
            tmp_names[my_name] = "2"
        else:
            tmp_names[my_name] = str(int(tmp_names[my_name])+1)
            lock_names.append(my_name)

print "用户输入错误记录%s"%(tmp_names)
print "被锁定的账号：%s"%(lock_names)
