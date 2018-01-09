#coding=utf-8

# 作者：杨公旺
# 时间：2017-11-27

j = 0
count=0
arr = [49,38,65,97,76,13,27,49,89,79,190,789,89]
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print arr
        count = count +1
print count


if pwd == password:
   print "登录成功"
      break
else:
print "输入错误"





num_list = [8,2,4,5,4,6,36]

while True:
    my_input = raw_input("请输入add/del/p:")
    if my_input != "add" or my_input != "del" or my_input != "p" or my_input != "exit":
        print "您只能输入add、del、p或exit"
        break


    if my_input == "add":
       my_number = raw_input("请输入您要插入的值：")
           num_list.append(my_number)
           print "当前列表是%s"%(num_list)
    if my_input == "del":
       if len(num_list)>0
           num_list.pop()
           print "当前列表是%s"%(num_list)
        else:
           print "列表为空，不允许删除操作"
    if my_input == "p":
           print "当前列表是%s"%(num_list)
    if my_input == "exit":
        break