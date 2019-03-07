# -*- coding:utf-8 -*-
#_str_:当使用print打印对象的时候会自动调用对象的str方法
class Person(object):
    #给对象添加属性并对属性进行初始化
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #返回对象的描述信息
    def __str__(self):
        #返回字符串信息
        return "我叫%s 年龄：%d" %(self.name,self.age)
#创建对象
#调用init方法使用位置参数方式传参
# person = Person(18,'刘理')
#使用关键字方式进行传参
person = Person(name='liu',age=18)
# print(person.age,person.name)
print(person) #输出对象的内存地址：<__main__.Person object at 0x0115D9F0>


