# -*- coding:utf-8 -*-
#缺省参数：在函数定义的时候参数就有值，这样的参数叫做缺省参数

#提示：如果给缺省参数传值，就是传入的值。如果不给缺省参数传值那么就使用默认值

def sum_num(num1,num2=1):
    result = num1 + num2
    return result
#没有给函数的第二个参数传值，那么就使用默认值（缺省值）
value = sum_num(1,5)
print(value)