# -*- coding:utf-8 -*-

#调用函数传参的方式有:1.使用位置参数方式传参，2.使用关键字参数方式传参

def show(name,age):
    print(name,age)
#positional argument ,丢失调用时候的一个位置参数

#使用位置参数方式传参必须按照函数参数的顺序去传参
show('liu',22)

#使用关键字参数传参,可以不按照函数参数的顺序传参
show(name = 'liu',age = 18)


#前面使用位置参数，后面使用关键字传参

#提示：如果前面使用关键字传参后面必须是关键字方式传参

show(name='liu',age=18)