# -*- coding:utf-8 -*-
#匿名函数：使用lambda关键字定义的匿名函数

# lambda 定义参数 ： 返回值
result = (lambda x,y : x+y)(1,2)
print(result)


# 一般使用变量保存匿名函数
func = lambda x,y : x*y

result = func(1,2)

print(result)

#匿名函数的应用场景，简化代码

def is_os(num):
    if num % 2  == 0:
        return True
    else:
        return False
result = is_os(1)
print(result)


#简化代码
new_func = lambda num: True if num  % 2 == 0 else False

result = new_func(4)

print(result)
#对字典列表排序的时候还可以使用匿名函数
# item['age']:根据字典中的age对应的值进行排序
#默认是从小到大进行排序
my_list = [{'name':'zs','age':8},{'name':'ls','age': 19}]
# my_list = [1,4,2]
my_list.sort(key=lambda item:item['age'],reverse=False)
print(my_list)

#匿名函数也是函数