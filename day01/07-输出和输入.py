# -*- coding: utf-8 -*-
print("Hello world")

my_str1 = 'hello'
my_str2 = 'world'

#提示：输出多个参数，多个参数之间默认使用空格做分隔
print(my_str1,my_str2)

print(my_str1,my_str2,sep='&')

#print默认输出信息后会换行
print('hello',end=' ')
print('world')

print('换行\nhh')

#输入：py3里面使用input
name = input('请输入您的姓名')
#提示：input返回的数据都是字符串
print(name, type(name))


