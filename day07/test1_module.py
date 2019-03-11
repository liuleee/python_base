# -*- coding:utf-8 -*-
#定义全局变量
g_score = 100

def show_info():
    print("show_info")

def sum_num(num1,num2):
    result = num1 + num2
    return result

#执行的这个模块就是主模块

#查看模块名
print(__name__)

#测试sun_num是否有问题
#判断是否为主模块
if __name__ == "__main__":
    value = sum_num(1, 3)
    print("2::",value)
