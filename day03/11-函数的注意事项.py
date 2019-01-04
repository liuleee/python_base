# -*- coding:utf-8 -*-
#函数的注意事项：1.函数名不能相同，py中没有覆盖。2.变量名不能和函数名相同

def show():
    print('好累啊')
def show(msg):
    print(msg)

#定义了第二个函数名和第一个函数名相同，那么第一个函数名不能使用
# show(111)

#定义变量名和函数名相同 xxx
show = 10
print(show)
show('ffff')