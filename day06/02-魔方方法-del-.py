# -*- coding:utf-8 -*-
import time
#__del__ :当对象释放的时候会自动调用__del__方法

#1.程序退出，程序中使用的对象全部销毁
#2.当前对象的内存地址没有变量使用的时候，那么对象会销毁
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __del__(self):
        print("对象释放了",self)
#第一种情况,程序退出，程序中使用的对象全部销毁
#创建对象
person_xiao = Person('小明',20)
print(person_xiao)


#2.当前对象的内存地址没有变量使用的时候，那么对象会销毁
#删除变量
del person_xiao

#引用计数：内存地址被变量使用的次数，当前引用计数为0，表示对象销毁
time.sleep(3)
print('outttttttttt')
