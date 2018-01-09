# -*- coding: utf-8 -*-

num = 1
L = []
tmp = []

#  ‰»Î
print "Input 10 numbers£°"
while num <=10:
    x = int(raw_input("Input [{0}]: ".format(num)))
    L.append(x)
    num += 1

print "The original list is {0}".format(L)

# ≈≈–Ú
for i in range(10):
    for j in range(9):
        if L[j] >= L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
# »•÷ÿ
for k in L:
    if k not in tmp:
        tmp.append(k)
print "The re-order list is {0}".format(tmp)
