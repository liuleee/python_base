# -*- coding:utf-8 -*-
class Person(object):
    def show(self):
        print('我是人类')

class Plane(object):
    def show(self):
        print('我是飞机')
    def fly(self):
        print('我可以飞')

class Student(Person,Plane):
    def show(self):

        #方法重写也可以使用super,调用父类的方法
        super(Student, self).show()


student = Student()
student.show()