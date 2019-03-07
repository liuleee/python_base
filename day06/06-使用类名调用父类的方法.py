# -*- coding:utf-8 -*-
class Animal(object):
    #对象方法
    def run(self):
        print('动物跑起来了')

class Dog(Animal):

    # def run(self):
    #     print('小狗跑起来了')

    def shut(self):
        #再次调用父类方法
        #1.self,前提当前类没有父类的方法，否则调用的是当前类的方法
        # self.run()
        #2.使用父类的类名,需要传入实例对象
        # Animal.run(self)
        #3.super调用父类的方法
        #根据指定类dog，在类继承链中获取下一个类animal
        #1.Dog表示根据指定类找类继承链中的下一个类
        #2.self表示获取self对象类型的类继承链
        #提示：super不一定是你直接继承的父类
        #提示：当继承直接理解成是继承的父类没有问题，但是多继承就有可能不是
        #提示：调用的是父类的方法，但是不一定是你直接继承父类的方法
        super(Dog, self).run()
        print(self.__class__.mro())
        print('wwwww')

dog = Dog()
dog.shut()
# dog.run()