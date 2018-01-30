#!/usr/bin/env python
#coding: utf8

def outer(func):
    def inner():
        print 'inner'
        ret = func()
        print 'outer'
        return ret
    return inner

# def outer(func):
#     def inner(*args,**kwargs):
#         print 'inner'
#         ret = func(*args,**kwargs)
#         print 'outer'
#         return ret
#     return inner

def login_required(func):
    def wrapper():
        print 'inner login_required'
        ret = func()
        print 'outer login_required'
        return ret
    return wrapper

def test1():
    print 'test1'

@outer
def test2():
    print 'test2'

# outer(test1)()
# test2()
# login_required(test1)()

@outer
@login_required
def test3():
    print 'test3'

test3()