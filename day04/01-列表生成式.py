# -*- coding:utf-8 -*-
#列表生成式：通俗理解使用for循环快速创建一个列表，最终要获取一个列表

# my_list = []
# for value in range(1,5):
#     print(value)
#     my_list.append(value)
# print(my_list)
#列表生成式目的：快速创建一个列表
#列表推导式的语法格式
# my_list = [value for value in range(1,6)]
# print(my_list)

my_list = [value*2 for value in range(1,6)]
print(my_list)

#in 里面可以
result = [value + 'hello' for value in ['abc','ab']]
print(result)