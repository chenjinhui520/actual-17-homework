#encoding=utf-8

while True:
    user_input = raw_input('请输入10位数字(整数):')
    user_list = list(user_input)
    length = len(user_input)

    new_list=[]

    #去重，加入新列表
    if length==10 and (user_input.isdigit()):
        for i in user_list:
            if i not in  new_list:
                new_list.append(i)
        new_length=len(new_list)  #计算去重后列表的长度
        #冒泡排序
        for j in range(new_length-1):
            for x in range(new_length-1-j):
                if new_list[x]>=new_list[x+1]:
                    new_list[x],new_list[x+1]=new_list[x+1],new_list[x]

        #将列表转为数字
        new_number=''
        for n in new_list:
            #这个是单纯将字符串拼接，然后转换为数字，需要就将new_number初始化
             new_number+=n
            #这个是转换为数字后相加,需要初始化new_number为int
            #new_number+=int(n+'0'*(new_length-new_list.index(n)-1))

        print '去重排序后的列表list为： %s'%(new_list)
        print '去重排序后的字符串str为： %s' %(new_number)
        print '去重排序后的数字int为： %s' %(int(new_number))
        break
    else:
        print '抱歉，你输入的不是10位整数.请重新输入'
