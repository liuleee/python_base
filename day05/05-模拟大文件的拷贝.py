# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
#1.打开源文件读取数据
#rb是比较通用的模式，可是兼容不同类型的文件
src_file = open('3.txt',"rb")
#循环读取文件中的数据
#2.打开目标文件准备写入数据
#扩展：可以指定拷贝后的文件路径
dst_file = open('3[fil].txt','wb')
#把源文件中的数据写入到目标文件
#循环读取文件中的数据
while True:
  file_data = src_file.read(1024)#不重复读取
  # 判断数据是否读取完成
  # if len(file_data) > 0:
  #判断二进制是否有数据：
  if file_data:
      #表示有数据
      #要把源文件中的数据写入到文件中
      dst_file.write(file_data)
  else:
      print('判断数据读取完成',file_data)
      break


#关闭文件
dst_file.close()
src_file.close()
