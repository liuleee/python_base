# -*- coding:utf-8 -*-
class Person(object):
    #私有的类属性
    __type = "黄种人"
    #定义对象方法：在方法的参数里面有self表示对象方法
    def show(self):
        print("我是人类")

    # 定义类方法：cls表示当前类
    #类方法只能修改类属性
    @classmethod
    def show_info(cls):
        print(cls)
        print("我是一个类方法")

    # 定义一个静态方法，提示：静态方法和当前对象和当前类没关系，不用使用self，cls
    @staticmethod
    def show_msg():
        print("我是一个静态方法")

    # 应用场景：类方法可以修改类属性
    @classmethod
    def set_type(cls,type):
        cls.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type

   #---对象方法是最通用的方法，可以修改对象属性和类属性
    def instance_set_type(self,type,name):
       # 获取对象所对应的类
        self.__class__.__type = type
        self.name = name

    def instance_get_type(self):
        print(self.name)
        return self.__class__.__type



#创建对象
p = Person()
p.show()
p.show_info()
p.show_msg()

p.set_type("白种人")

result = p.get_type()
print(result)

p.instance_set_type("黑种人","lk")
print(p.instance_set_type())
