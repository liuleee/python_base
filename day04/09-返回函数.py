# -*- coding: utf-8 -*-

#函数的嵌套
#返回函数：在函数里面返回一个函数
def show():
    def inner():
        print('hhh')
        #返了一个函数
    return inner
#获取返回的函数
new_func= show()
#执行返回的函数
new_func()

def calc(operation):
    if operation == '+':
        def sum_num(num1, num2):
            result = num1 + num2
            return result
        return sum_num
    if operation == '-':
        def sum_num(num1, num2):
            result = num1 - num2
            return result
        return sum_num
#获取返回函数
new_func = calc('-')
#给返回函数赋值
result = new_func(1,2)
print(result)