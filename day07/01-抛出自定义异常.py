# -*- coding:utf-8 -*-
#自定义异常类
class CustomException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return "我是自定义异常,因为数据不是a,异常数据为%s"%self.content

content = input("请输入数据")
if content != "a":
    raise CustomException()  #抛出异常

