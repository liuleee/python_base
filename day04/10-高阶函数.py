# -*- coding: utf-8 -*-
#高阶函数：当一个函数的参数可以接收另外一个函数，或者返回一个函数，那么这个函数就叫做高阶函数
#高阶函数针对的是接收的函数，返回的是函数，类似这样的函数统称为高阶函数

def sum_num(num1,num2):
    result = num1+num2
    return result
# new_func = sum_num(2,3)
# print(new_func)

#高阶函数，因为接收的参数是一个函数
def calc_num(num1,num2,new_func):
    value = new_func(num1,num2)
    return value

result = calc_num(1,2,sum_num)
print(result)


#高阶函数，还可以返回一个函数

def test(new_func):
    new_func()
    def inner():
        print('我是内部函数')
    return inner

def show_msg():
    print('天气好闷热！')


new_func = test(show_msg)
new_func()