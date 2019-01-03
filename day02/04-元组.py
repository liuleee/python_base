# -*- coding: utf-8 -*-
#元组：以小括号表现形式的数据集合，比如（1,2，‘abc)
#元组也可以存放任意数据
#元组指定根据下标获取数据，不能对元组进行数据的修改
my_tuple = (1,4,'abc','True',1.2)
print(my_tuple,type(my_tuple))


#根据下标取值
value = my_tuple[-1]
print(value)


#元组不能根据下标删除数据
#del my_tuple[2]
#不支持修改
# my_tuple[0] = 2
# print(my_tuple)

my_tuple = (1,[2,5])
my_list = my_tuple[1]
del my_list[0]
print(my_tuple)

#如果元组中只有一个元素，那么需要加上一个逗号，
my_tuple = (5,)
print(my_tuple,type(my_tuple))

#判断数据是否存在
my_tuple = (5,10)
result = 5 in my_tuple
print(result)


result = my_tuple.count(0)
print(result)