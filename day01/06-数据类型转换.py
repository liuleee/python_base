# -*- coding: utf-8 -*-
num = 10
my_str = '10'

# 把字符串转为int类型
num2 = int(my_str)

# print(type(num2))

s = num + num2

# print(s)

my_float_str = '3.14'
print(type(my_float_str))
num3 = float(my_float_str)
print(type(num3))


num4 = 4.55
# 浮点数转int型时，只取整数
num5 = int(num4)
print(num5)

# eval:获取字符串中的 原始 数据
my_str = '5'
value = eval(my_str)
print(value)
print(type(value))

#int类型和float类型计算时int类型会转换成float类型
result = num + num3
print(result)

'''
 day01 : 55:09
'''