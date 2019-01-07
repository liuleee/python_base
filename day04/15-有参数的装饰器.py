# -*- coding: utf-8 -*-
def get_decorator(char):
    def decorator(func):
        def inner():
            print(char*10)
            func()
        return inner
    return decorator

#把@后面的操作相当于执行了函数，返回一个撞死去
@get_decorator('a')  #有参数的装饰器
def show():
    print('11111')

show()