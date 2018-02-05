#!coding: utf8

class Animal(object):
    def __init__(self,name,age,sex,type='牧羊犬'):
        self.name = name
        self.age = age
        self.sex = sex
        self.type = type

    def getName(self):
        return '名字是：%s' % self.name

    def getType(self):
        return '犬种是：%s' % self.type
