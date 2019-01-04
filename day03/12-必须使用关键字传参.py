# -*- coding:utf-8 -*-


###   *后面的必须使用关键字传参
def show(address,sex,*,name,age):
    print(address,sex,name,age)
    print('我叫%s 年龄%d'% (name,age))

#使用位置参数传参
# show('liu',18)
#使用关键字参数传参
show('上海','m',name='caocao',age=66)