# -*- coding:utf-8 -*-

#文件的访问模式：
# r:只读 ,如果文件不存在会崩溃
# w.只写
# a:追加写入
# #rb:以二进制方式读取文件数据
# #wb:以二进制方式写入文件数据
# ab:以二进制方式追加写入文件数据
# r+,w+,a+,支持读写，但是要看前面的主模式
# rb+,wb+,ab+支持二进制读写操作




# -----r模式----
#打开文件使用open
# file = open('1.txt','r',encoding='utf-8')  #默认是r,r是只读
# #读取文件中的数据
# content = file.read()
# print(content)
# #关闭文件
# file.close()

#------w模式----
#提示：如果文件不存在，那么会创建一个文件并打开，然后写入数据
#提示：如果文件存在，那么会把文件中原有文件清空，然后在写入
#注意点：如果使用w模式每次打开数据会先清空文件，再写入


#tip:如果在windows开发python,那么需要制定编码格式
#打开文件使用open
# file = open('1.txt','w',encoding='utf-8')  #默认是r,r是只读
# #读取文件中的数据
# file.write('哈哈'+'\n')
# #打开文件后多次写入数据不会覆盖前面的数据
# file.write('world')
# #关闭文件
# file.close()

#-------------a模式追加写入数据-----------
# file = open('1.txt','a',encoding='utf-8')
# file.write('小土豆')
# file.close()
#在python2里面不支持文件中有中文，需要指定编码格式(顶部）

#----rb模式：以二进制方式读取数据----
# file = open('1.txt','rb')
# file_data = file.read()
# #对二进制数据utf-8进行解码:二进制到字符串
# content = file_data.decode('utf-8')
# print(content)
# file.close()

#----wb模式：以二进制方式写入数据----
# file = open('1.txt','wb')
# #对字符串进行utf-8编码得到二进制数据
# content = 'hello 哈哈'
#
# file_data = content.encode('utf-8')
# file.write(file_data)
#
# file.close()

#----ab模式：以二进制方式追加写入数据----
file = open('1.txt','ab')

#对字符串进行utf-8编码得到二进制数据
content = 'hello 哈哈'

file_data = content.encode('utf-8')
file.write(file_data)

file.close()


#----------r+读写----------
#为了兼容不同操作系统，只要没看到b模式可以使用encoding指定编码格式

file = open('1.txt','r+',encoding='utf-8')

#提示：写入数据时候不会先清空数据，把指定数据替换成写入数据，且字节相同
result = file.read()
print(result)

file.write('哈哈哈')
file.close()



