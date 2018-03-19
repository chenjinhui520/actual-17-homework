#encoding: utf-8

x = 1
y = 1

while x <= 9:
    while y <= x:
        print(str(y) +'*'+ str(x) + '=' + str(x * y), end='\t')
        y += 1
    print()
    x += 1
