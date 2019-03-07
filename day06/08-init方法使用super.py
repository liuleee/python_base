# -*- coding:utf-8 -*-
class A(object):
    def __init__(self,name):
        print('A')
        self.name = name

class B(A):
    #如果子类提供调用的方法，那么不会主动调用父类的方法
    def __init__(self,subject):
        #调用父类的init方法,使用类名调用
        # A.__init__(self,'李四')
        print(self.__class__.mro())
        super(B, self).__init__('王五')

        #简写super ()->super(B,self)
        super().__init__('梦继')
        print('B')
        self.subject = subject
    def show(self):
        print("我是B类")

b = B('python')
print(b.name)
b.show()