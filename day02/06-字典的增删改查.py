# -*- coding: utf-8 -*-

#字典是无序的，列表有序
#无序：定义的顺序和输出的数据一致
my_dict = {}
print(my_dict,type(my_dict))

#添加键值对，key不存在字典里面是添加

my_dict['name'] = 'liulee'
my_dict['age'] = 18
my_dict['sex'] = '男'
my_dict['addr'] = '成都'
print(my_dict)
#修改键值对，key存在就是修改

my_dict['addr'] = '重庆'
print(my_dict)

#删除键值对
del my_dict['age']
print(my_dict)

#随机删除
# result = my_dict.popitem()
# print(result,my_dict)

value = my_dict.pop('name')
print(value,my_dict)

#判断key是否存在
result = 'sex' in my_dict
print(result)

result = '男' in my_dict.values()
print(result)

'''
1:35:46
'''