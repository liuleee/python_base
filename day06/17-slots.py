# -*- coding:utf-8 -*-
#slots ：指明创建对象的时候不能再添加其他属性，只能指定属性

class Student(object):
    __slots__ = ("name","age")
    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student("李四",20)


print(stu.name,stu.age)