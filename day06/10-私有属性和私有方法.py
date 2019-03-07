# -*- coding:utf-8 -*-
#在属性名和方法名前面加上__那么定义的属性和方法就是私有属性和私有方法

class Person(object):
    def __init__(self,name,age):
        self.name = name
        #私有属性只能在本类内部使用，在类外面不能使用

        #私有属性只能在init方法里面添加
        self.__age = age

    def show(self):
        print(self.name)

    def __money(self):
        print('100www')

person = Person(name='liu',age=18)
print(person.name)
# 私有属性在外界访问不了
# print(person.__age)


person.show()
#私有方法在外界访问不了
# person.__money()

#查看对象中的属性信息
print(person.__dict__)

#本意是修改私有属性
#这里不是修改了私有属性，而是给对象添加了__age的对象属性
person.__age = 22
print(person.__age)

#查看私有方法
print(person.__dict__)

#在python里面私有属性和私有方法没有做到绝对私有

#非常规操作，不建议以后使用
person._Person__age = 34