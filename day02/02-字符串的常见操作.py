# -*- coding: utf-8 -*-

#字符串定义：只要用引号引起来的数据都叫做字符串

my_str = 'hello'

# 根据指定数据查找对应的下标（索引
result = my_str.index('l')
print(result)

# 根据指定数据查找对应的下标（索引
result = my_str.find('h')
print(result)

#find如果没有找到制定数据，返回的结果是-1，而index会崩溃


#统计字符串的个数
result = len(my_str)
print(result)

#统计某个字符串出现的次数
result = my_str.count('l')
print(result)

#替换指定数据
result = my_str.replace('l','x')
print(result)

#分割数据
my_str = 'a,b,c'
result = my_str.split(',')
print(result)

#判断数据是否以指定字符串开始
my_url = 'http://baidu.com'
result = my_url.startswith('http')
print(result)

result = my_url.endswith('com')
print(result)

#需求：把字符串以指定字符串分割数据成为三部分
my_str = 'aabbccc'
result = my_str.partition('bb')
print(result)

#join：根据指定字符串拼接数据，前提是最终的数据是字符串
#指定字符串数据

flog_str = '-'
my_str ='abc4567'
result = flog_str.join(my_str)
print(result)

my_list = ['1','3','5']
result = flog_str.join(my_list)
print(result)


#去除空格
my_str = ' hello '
result = my_str.strip()
result = my_str.lstrip()
result = my_str.rstrip()
print(result)

#去除指定数据
my_str = 'ahelloa'
result = my_str.strip('a')
print(result)