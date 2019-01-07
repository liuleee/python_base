# -*- coding: utf-8 -*-

#装饰器本质上就是一个函数，可以给原函数的功能上进行拓展，这样的好处是，不改变原函数的定义及调用的操作
#装饰器——》通过闭包完成的
def decorator(new_func):

    def inner():
        print('-'*10)
        new_func()
        #返回的函数是闭包
    return inner
#在使用@decorator的时候装饰器的代码就会执行
@decorator
#使用装饰器，装饰下面的函数
def show():
    print('aaaaaaa')

show()

#装饰器的最大作用是扩展原有函数功能


# show = decorator(show)
# show()