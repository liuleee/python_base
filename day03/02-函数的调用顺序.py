# -*- coding:utf-8 -*-

#定义函数：函数的定义是不会执行函数体里面的代码的
def show(name,age):
    print('我叫：%s 年龄：%d' %(name,age))

#调用函数，执行代码

show('liu',22)
print('aaa')

#总结：函数调用的时候先去给函数传参，当函数体里面的代码执行完成以为会回到函数调用的地方，然后代码在往下执行