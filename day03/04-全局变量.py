# -*- coding:utf-8 -*-
#全局变量：在函数外定义的变量叫做全局变量，全局变量可以做不同函数内使用

score = 100
def show():

    #在这里不是对全局变量进行了修改，而是定义了一个局部变量
    # score = 99
#修改全局变量
    global score #表示要对全局变量score进行数据修改
    score = 99
    print('分数',score)
show()

def show_score():
    print('数学分数',score)
show_score()

#全局变量变量可以在不同函数内共享全局变量的数据