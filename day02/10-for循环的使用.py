# -*- coding:utf-8 -*-

#获取容器类型（字符串，列表，元组，字典，set)中每个数据使用for循环最简单

# my_str = 'abc'
# for value in my_str:
#     print(value)

# my_list = ['apple','peach','banana','pearl']
# for value in my_list:
#     print(value)

#循环遍历的时候下标和数据都需要，可以使用enumerate
my_list = enumerate(['apple','peach','banana','pearl'])
# for value in my_list:
#     print(value[0],value[1])

#index,value获取的是列表中的每一个值，就是拆包
for index,value in my_list:
    print(index,value)


#取下标神器enumerate
for value in enumerate((1,5)):
    print(value)
#遍历数据的时候需要下标可以通过enumerate


#默认遍历是key
my_dict = {'name':'zhang','age':18}
# for key in my_dict:
#     print(key,my_dict[key])

#其实遍历的是每一项字典中的键值对
for key,value in my_dict.items():
    print(key,value)

my_set = {1,5,7}
for value in my_set:
    print(value)