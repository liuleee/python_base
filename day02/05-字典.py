# -*- coding: utf-8 -*-
#字典：以大括号{}表现形式的键值对数据的集合比如{’name':'张三’，‘age':18}
#key一般都是字符串，key只能是不可变类型：数字，字符串，元组。不能使用可变：列表，字典

my_dict = {'name':'zhang','age':18}
print(my_dict,type(my_dict))

#通过key获取对于value的值，key值在字典里面是唯一的

value = my_dict['name']
age = my_dict['age']
print(age)
#my_dict['name],my_dict.get('sex'),中括号方式取值key不存在会崩溃，get方式取值不成功返回null,或默认值

result = my_dict.get('sex',6666666666)
print(result)

