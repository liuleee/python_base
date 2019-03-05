# -*- coding:utf-8 -*-
#打开元数据
src_file = open('3.txt','rb')
#读取源数据
file_data = src_file.read()
#打开目标数据
dst_file = open('31.txt','wb')
#写入源数据
dst_file.write(file_data)
#关闭
src_file.close()
#关闭
dst_file.close()