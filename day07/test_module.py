# -*- coding:utf-8 -*-
#定义全局变量
g_num = 10

#定义函数
def show():
    print("我是一个函数")

#定义类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_msg(self):
        print(self.name,self.age)
