# -*- coding: utf-8 -*-

#装饰带有参数的函数

#装饰器要接收一个函数，就是以后要执行的函数

#定义一个装饰器函数
def decorator(func):
    def inner(num1,num2):
        print('计算结果如下')
        return func(num1,num2)
    return inner
@decorator #->sum_num = decorator (show)
def sum_num(num1,num2):
    result = num1 + num2
    # print(result)
    return result

@decorator
def sum_msg(num1,num2):
    print(num1,num2)

#z执行返回的inner函数，并传了
# result = sum_num(1,2)
# print(result)


#sum_msg执行这个函数相当于装饰器里面的inner函数
result = sum_msg(1,4)
print(result)


####装饰带有参数的函数，里面函数就有什么参数