# -*- coding:utf-8 -*-
#read ,readline,readlines ,读取文件的操作

# file = open('1.txt','r',encoding='utf-8')
# #读取指定长度数据：提示：r读取的是内容长度
# #提示：如果是r模式读取的是指定数据的长度
# content = file.read(1)
# print(content)
# file.close()

file = open('1.txt','rb')
#读取指定长度数据：如果是rb模式读取的是字节数
#提示：如果是r模式读取的是指定数据的长度

content = file.read(4)
#在utf-8编码格式下，一个汉字占用3个字节，一个字母和数字占用一个字节
file_data = content.decode('utf-8')
print(file_data)
file.close()


#根据指定的文件指针读取数据
file = open('1.txt','rb')
#查看文件指针的位置
result = file.tell()
#设置文件指针的位置
file.seek(7)
result = file.tell()
print(result)
file_data = file.read()
content = file_data.decode('utf-8')
print(content)
file.close()