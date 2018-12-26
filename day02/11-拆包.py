# -*- coding:utf-8 -*-
#拆包：通俗理解把容器类型中的每一个数据使用不同变量进行保存

my_str = 'abc'
#变量的个数要与容器的个数一致
a,b,c = my_str
print(a,b,c)

my_list = [1,5]
num1,num2 = my_list
print(num1,num2)

#字典默认取值为key值
my_dict = {'name':'lee','age':16}
num1,num2 = my_dict
print(num1,num2,my_dict[num1],my_dict[num2])

my_set = {3,5}
num1,num2 = my_set
print(num1,num2)