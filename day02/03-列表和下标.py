# -*- coding: utf-8 -*-
#列表：以中括号[]表现形式的数据集合比如[1,4]
#提示：列表里面可以放入任何类型数据
my_list = [1,1.22,'BC',True]
print(my_list, type(my_list))

#获取列表中的数据可以根据下标获取
value = my_list[0]
print(value)

#python中的下标：下标其实就是一个标号，可以根据标号找到某个数据
#python里面的正数下标，默认从0开始，负数下标-1表示倒数第一个

#根据下标取元素
result = my_list[-1]
result = my_list[-3]
result = my_list[3]

print(result)

#列表的增删改查
my_list = []
#向列表中追加指定数据
my_list.append(1)
print(my_list)
my_list.append('大家好')
print(my_list)

#插入指定数据
my_list.insert(1,'a')
print(my_list)

my_list1 = ['apple','watermalon','mongo']
# my_list.append(my_list1)
# print(my_list)

#extend
my_list.extend(my_list1)
print(my_list)

#修改数据：根据下标

my_list[0] = 'banana'
print(my_list)

my_list[-1] = 'peach'
print(my_list)

#remove删除指定数据
my_list.remove('peach')
print(my_list)

#根据下标删除指定数据:下标要合法
del my_list[0]
print(my_list)

#根据下标删除数据，并返回删除的数据
#pop不指定下标默认删除倒数第一个数据
result = my_list.pop(1)
print(my_list)

#判断指定数据是否在列表里面
result = 'a' not in my_list
print(result)

result = my_list.index('a')
print(result)

#根据指定数据获取数据在列表中的个数
count = my_list.count('a')
print(count)


