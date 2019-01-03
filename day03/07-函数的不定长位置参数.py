# -*- coding:utf-8 -*-
#不定长位置参数，不定长关键字参数

#不定长参数：调用函数的时候不确定的传入多少个，可能是0个或者多个参数
#定义函数的时候，1.不定长位置参数，2.不定长关键字参数

########定义不定长位置参数(*args),保存为元组
#
# def sum_num(*args):
#     #args会把调用函数传入的位置参数封装到一个元组里面，如果没有传入就是一个空元组
#     print(args,type(args))
#     sum = 0
#     for value in args:
#         sum += value
#     return sum
# value = sum_num(5,4)
# print(value)

#总结：函数的调用
#1.做自加遍历时需要加上一个初始变量
#2.遍历结束后，记得return结果
#3.调用时记得给变量保存
#4.打印

#位置参数不能传入关键字参数
#

#------------不定长关键字参数---------保存为字典-----

def sum_msg(**kwargs):
    #kwargs会把调用函数传入的关键字参数封装到一个字典里面，如果没有传入就是一个空字典
    print(kwargs,type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
#调用的是不定长关键字参数的函数
sum_msg(a = 12,b = 2)
