# -*- coding:utf-8 -*-
#单继承：子类只继承一个父类
#子类继承父类可以使用父类的方法和属性
#继承的好处：是子类可以复用父类的代码
class Person(object):
    def __init__(self):
        self.name = 'liu'
        self.age = 20
    # 对象方法，当前方法参数有self表示对象方法
    def show(self):
        print(self.name,self.age)
#student继承Person
#父类（基类），子类（派生类）
class Student(Person):
    pass
student = Student()
student.show()
print(student.name,student.age)