# -*- coding: utf-8 -*-
my_list = [1,4,5,4]

my_tuple = (5,7)

my_set = {4,9}

#把列表转成集合
result = set(my_list)
print(result,type(result))

#把元组转成集合
result = set(my_tuple)
print(result,type(result))

#把列表转成元组
result = tuple(my_list)
print(result,type(result))

#把集合转成元组
result = tuple(my_set)
print(result,type(result))

#把集合转成列表

result = list(my_set)
print(result,type(result))

#把元组转列表
result = list(my_tuple)
print(result,type(result))