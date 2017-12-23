# -*- coding: UTF-8 -*-
while True:
 def zhuce():
 	handler = open('user.txt','a+')
 	print '欢迎使用注册系统'
	name = raw_input('请输入用户名：')
	if not name.isspace() and name:
        	pswd1 = raw_input('请输入密码:')
        	pswd2 = raw_input('请确认密码:')
        	if pswd1 == pswd2:
                	handler.write(name + ':' + pswd1 + '\n')
        	else:
                	print '输入两次密码不一致'
 	else:
        	print '用户名错误，退出！'
 	handler.close()

 def denglu():
	rhandler = open('user.txt','r')
	ndict = {}
	for i in rhandler.readlines():
        	i = i.strip('\n')
        	ndict[i.split(':')[0]] = i.split(':')[1]
	rhandler.close()
	name = raw_input('请输入用户名:')
	if not name.isspace() and name:
        	if ndict.has_key(name):
                	pswd = raw_input('请输入密码:')
                	if pswd == ndict[name]:
                	        print '登录成功-_-'
			else:
                        	print '登录失败囧'
        	else:
                	print '没有这个用户'
	else:
        	print '用户名不能为空！'
 xuanze = raw_input('请输入register／login／exit:')
 if xuanze == 'register':
	zhuce()
 elif xuanze == 'login':
	denglu()
 	break
 elif xuanze == 'exit':
	break
 else:
	print '请输入正确的字符'
