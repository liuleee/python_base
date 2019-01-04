# -*- coding:utf-8 -*-


#定义不定长位置参数函数：
def show_msg(*args):
    # print('show_msg:',args)
    for value in args:
        print(value)

#定义不定长的位置参数函数
def show(*args):
    # print('show:',args)
    # show_msg(args)
    #解决方法，对元组进行拆包
    show_msg(*args)
show(1,2)