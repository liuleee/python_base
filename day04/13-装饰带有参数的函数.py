# -*- coding: utf-8 -*-
def decorator(func):
    def inner(num1,num2):
        print('计算结果如下')
        func(num1,num2)
    return inner
@decorator
def sum_num(num1,num2):
    result = num1 + num2
    # print(result)
    return result
sum_num(1,2)


#装饰带有参数的函数，里面函数就有什么参数