# -*- coding: utf-8 -*-
#变量：存储程序数据的容器

# 变量名 = 数据

score = 100
print(score)

name = '张三'
print(name)

pi = 3.14
print(pi)

#在python里面无需制定python类型，会根据数据自动推导数据类型

is_ok = True
print(is_ok)

#通过type查看变量的类型

score_type = type(score)
name_type = type(name)
pi_type = type(pi)
is_ok_type = type(is_ok)

print(score_type)
print(name_type)
print(pi_type)
print(is_ok_type)


#常用的数据类型有int ,str,float,bool,list tuple,dict,set