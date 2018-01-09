first_num = raw_input("please input first number:")
second_num = raw_input("please input second number:")
third_num = raw_input("please input third number:")
fouth_num = raw_input("please input fouth number:")
fifth_num = raw_input("please input fifth number:")
sixth_num = raw_input("please input sixth number:")
seventh_num = raw_input("please input seventh number:")
eighth_num = raw_input("please input eighth number:")
ninth_num = raw_input("please input ninth number:")
tenth_num = raw_input("please input tenth number:")
num_list = []
for i in [first_num,second_num,third_num,fouth_num,fifth_num,sixth_num,seventh_num,eighth_num,ninth_num,tenth_num]:
  if int(i) not in num_list:
    num_list.append(int(i))
print num_list
for j in range(0,len(num_list)):
  for i in range(0,len(num_list)-j-1):
    if num_list[i] > num_list[i+1]:
      num_list[i],num_list[i+1] = num_list[i+1],num_list[i]
print num_list

上面是第一次的思路，虽然也实现了，但是在第一次让用户输入数字的时候用的代码太多，所以有了第二次的思路。就是一直奇怪，为什么不用int转型，列表里就会是加了引号的数字，也就是按照字符串类型加进列表了。
count = 0
num_list = []
while count < 10:
  input_num = raw_input("please input a number:")
  count = count + 1
  if int(input_num) not in num_list: 
    num_list.append(int(input_num))
print num_list
for j in range(0,len(num_list)):
  for i in range(0,len(num_list)-j-1):
    if num_list[i] > num_list[i+1]:
      num_list[i],num_list[i+1] = num_list[i+1],num_list[i]
print num_list
