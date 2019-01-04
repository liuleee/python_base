# -*- coding:utf-8 -*-

#切片：根据下标的范围获取一部分数据  比如列表，字符串

my_str = 'hello'

# result = my_str[3]
# print(result)

#切片的使用格式

#数据【起始下标：结束下标：步长】

#提示：起始下标默认是0，结束下标是不包含，步长默认是q


#使用切片刀的方式获取一部分数据
result = my_str[1:3]
print(result)

result = my_str[:3]
print(result)
# 使用负数下标切片方式获取数据
# 可以获取倒数后面三个数据

result = my_str[-3:]
print(result)

#倒着取数据,步长是-1

my_str = 'hello'
result = my_str[-2:-5:-1]
print(result)

#倒着获取字符串的每个数据
result = my_str[ : : -1]
print(result)