# -*- coding: utf-8 -*-
age = int(input('请输入您的年龄：'))
#
# print('if语句开始判断了')
# if age >= 18:
#     #条件成立，if语句的代码才会执行
#     print('成年')
# else:
#     print('未成年')
#
# print('if语句结束判断了')


#if-else语句

#if-elif-else语句，可以判断多个条件

if age >= 15 and age<=17:
    print('少年')
elif age > 17 and age < 40:
    print('中年')
else:
    print('老年')

