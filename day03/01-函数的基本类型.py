# -*- coding:utf-8 -*-
# 函数就是实行某个功能的代码块，提高代码的复用性
#函数的四种类型


#无参数无返回值的函数
def show():
    print('大家好，今天的天气不好')
show()

#有参数无返回值的函数
def show(name,age):
    print('我的名字是%s，今年%d'%(name,age))
show('liu',18)

#无参数，有返回值
def return_val():
    msg = '好好学习，天天向上'
    return msg
#调用有返回值函数并使用变量进行保存
result = return_val()
print(result)

#有参数有返回的函数
def show_msg(name,age):
    msg = '我叫%s,%d岁' % (name,age)
    return msg
result = show_msg('liu',18)
print(result)
