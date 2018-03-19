#encoding: utf-8

import random

random_num = random.randint(0, 100)
print(random_num)
y = 1

while y < 6:
    x = int(input('请输入一个数字：'))
    if x < random_num:
        print('猜小了')
    elif x > random_num:
        print('猜大了')
    else:
        print('猜对了')
        break
    y += 1
if y >= 6:
    print('太笨了，下次再来')
