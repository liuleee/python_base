# -*- coding:utf-8 -*-

#函数嵌套：在函数里面再定义函数

def show():
    def test():
        print('hhhh')
        #函数内的函数必须在函数内使用，不能在函数外使用
    test()

show()