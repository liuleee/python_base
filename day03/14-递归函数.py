# -*- coding:utf-8 -*-
#递归函数：在函数里面调用函数本身

#递归函数的特点：1.传递。2.回归

#不能无限制传递，要有回归

#5！

def calc_num(num):
    # 当计算1的阶乘的不需要往下传递需要返回的结果
    if num == 1: #递归函数必须设置结束递归的条件及返回值
        return 1
    else:
        return num *calc_num(num-1)
result = calc_num(5)
print(result)

#不能无限递归调用，默认调用1000次