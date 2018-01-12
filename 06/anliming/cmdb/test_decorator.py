# encoding:utf-8
from functools import wraps

'''
以函数作为参数，返回这个函数

在所有函数之前执行一块代码
在所有函数之后执行一块代码
'''

def outer(func):
    @wraps(func)
    def inner():
        print '装饰器开始：%s'%func.__name__
        ret = func()
        print '装饰器结束.'
        return ret
    return inner

def login_required(func):
    @wraps(func)
    def inner1():
        print '登陆开始：%s'%func.__name__
        ret = func()
        return ret
    return inner1


def test1():
    print 'test1'

def test2():
    print 'test2'

@outer
@login_required
def test3():
    print 'test3'

test1()
test2()
test3()



