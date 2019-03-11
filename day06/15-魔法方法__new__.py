# -*- coding:utf-8 -*-
# __new__：当创建对象的时候会调用__new__方法
# __init__:对象创建完成会调用init方法给对象添加属性及初始化

#创建对象会自动创建两个方法，先调用new方法表四对象创建完成，然后创建new对对象初始化

class Student(object):
    #new方法里面的参数要兼容init方法里面的参数的
    def __new__(cls,*args,**kwargs):
        print("创建对象")
        print(args,kwargs)
        return object.__new__(cls)
    #对象创建完成了，给对象添加对象属性的
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("初始化")


stu = Student("李四",20)