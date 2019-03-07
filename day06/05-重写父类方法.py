# -*- coding:utf-8 -*-
#重写：子类继承父类，父类的方法满足不了子类的需要，可以对父类的方法进行重写
#重写的特点：1.j继承关系，2.方法名相同
class Person(object):
    def run(self):
        print('跑起来了')

class Student(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age

        #因为父类方法满足不了子类的需要，对其进行重写
    def run(self):
        print("%s跑起来了"%(self.name))

stu = Student('王五',18)

#调用方法的时候，先从本类去找，如果没有再去父类找，遵循mro的特点
stu.run()
