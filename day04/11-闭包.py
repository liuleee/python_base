# -*- coding: utf-8 -*-
#在函数嵌套的情况下，内部函数使用了外部函数的参数或者变量，并把这个函数返回，那么返回的函数可以称为闭包（对应的就是一个函数）’

def show(msg):
    num = 10
    def inner():
        print(num,msg)
    return inner
new_func = show('好好好')
# print(new_func)
new_func()

#闭包的应用场景，可以根据参数生成不同的返回函数（闭包——）
#通过闭包可以生成不同的函数

#闭包可以根据条件生成不同的函数

def hello(msg,count):

    def return_msg():
        result = msg * count
        return result
    return return_msg
    # result = msg*count
    # return result
new_func1 = hello('A',2)
new_func1()

new_func2 = hello('A',2)
new_func2()

print(new_func1,new_func2)
