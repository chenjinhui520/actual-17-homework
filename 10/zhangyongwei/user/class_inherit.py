#coding: utf8

# 先写一个父类
class Father(object):
    def __init__(self):
        self.name = '父亲'
    def vehicle(self):
        return  self.name + '有一辆兰博基尼'
    def house(self):
        return self.name + '还有一栋300平的别墅'

class Son(Father):
    def __init__(self,name):
        self.name = name


print