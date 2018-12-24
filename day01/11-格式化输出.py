# -*- coding: utf-8 -*-

#格式化符号 %s,%d,%f,%x
#%s:输出字符串
#%d:输出int类型数字
#%f:输出浮点数
#%x:输出16进制数据

name = '张三丰'
print('我叫%s'%name)

score = 100
print('成绩%d'%score)

pi = 3.1415926
#%f 默认保留6位小数
#%f会对数据进行四舍五入
print('圆周率%f'%pi)
print('圆周率%.2f'%pi)

num = 35
print("%x"%num)