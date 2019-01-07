# -*- coding: utf-8 -*-
def decorator1(func):
    def inner():#inner其实就是你封装传入函数的代码
        print('_'*30)
        func()
    return inner

def decorator2(func):
    def inner():#inner其实就是你封装传入函数的代码
        print('_*'*30)
        func()
    return inner

@decorator1
@decorator2
def show():
    print('AAA')
show()