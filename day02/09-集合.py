# -*- coding:utf-8 -*-
#集合set:以大括号表现形式的数据集合，集合里面不能有重复数据，集合也是无序

# 集合不能根据下标获取和修改数据，可以添加和删除数据

my_set = {1,4,'abc','hello'}
print(my_set)

#添加数据
my_set.add(5)
print(my_set,type(my_set))

#删除数据
# my_set.remove('abc')
# print(my_set)
#
# my_set.discard('hel9lo')

#总结：remove删除数据，数据必须存在，否则会崩溃。
#discard删除数据，数据不存在，会忽略，不会崩溃
print(my_set)
#测试
# my_set[0] = 3
# print(my_set)
#
# value = my_set[0]
# print(value)

for value in my_set:
    print(value)

#定义空的集合时不能直接使用{}大括号，因为大括号代表字典
my_set = set()
a = my_set.add(5)
print(a)

#元组不能修改数据，但是能添加和删除数据，不能根据下标删除和修改数据

#集合可以对容器类型数据去重

my_list = [1,5,1,4,5,9,7,8]
my_set = set(my_list)
print(my_set)

#list()列表，元组tuple()和集合set{}，三者直接可以相互转换