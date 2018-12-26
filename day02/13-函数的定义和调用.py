# -*- coding:utf-8 -*-
#函数定义的格式
# def 函数名(参数[可选])：
#     功能代码的实现

def show():
    print('I am liu,18yrs')
#调用函数
show()

#定义带有参数的函数，形参：形式参数&实参：实际参入的参数
def show(name,age):
    print('我叫%s,年龄%d'%(name,age))
#调用带有参数的函数
show('liu',34)
