# -*- coding: utf-8 -*-
 #偏函数：通俗理解知名函数的参数偏爱某个值这样的函数叫做偏函数
import functools
def show(num1,num2,num3=1):
    result = num1 + num2 + num3
    return result

result = show(1,2)

print(result)

#定义一个偏函数

def show_pian(num1,num2,num3=2):
    result =  show(num1,num2,num3)
    return result

result = show_pian(1,2)

print(result)

#指明函数的参数设置为某个值
#返回的函数就是偏函数
new_func = functools.partial(show_pian,num2=2)
result = new_func(3)

print(result)

#指明内置函数的参数偏爱某个值，生成一个偏函数
result = int('123')


###指明函数里面的参数偏爱某个值，那么返回的函数就是偏函数
new_func = functools.partial(int,base = 2)
result = new_func('11')
print(result)