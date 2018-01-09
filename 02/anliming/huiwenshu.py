#encoding=utf-8
while True:
    user_input = raw_input('pelese input a number:')
    user_list = list(user_input)
    length = len(user_input)
    if user_input.isdigit():
        if length==1:       #判断个位数
            print '恭喜，你输入的数字 "%s" 是回文数' %(user_input)
        else:
            for i in range(0, length / 2):                  #遍历
                if user_list[i] != user_list[-i - 1]:       #判断列表中的索引是否相等
                    if i == length / 2 - 1:                 #最后一次，打印输出
                        print '抱歉，你输入的数字不是回文数'
                else:
                    if i == length/2-1 :                    #最后一次，打印输出
                        print '恭喜撒花，你输入的数字 "%s" 是回文数 ' %(user_input)
    else:
        print '抱歉，请输入整数 '


