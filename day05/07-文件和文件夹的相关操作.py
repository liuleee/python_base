# -*- coding:utf-8 -*-
#创建文件
# file = open('4.txt','w',encoding='utf-8')
# # file.write('abc')
# # file.close()
#文件和文件夹操作相关的模块（py文件
import os
import shutil #文件操作的高级模块
#重命名,提示：目标文件必须存在
# os.rename('444.txt','4.txt')
#创建文件夹
# os.mkdir('AAA')
# os.rename('AAA','BBB')
#1.指定路径创建
# file = open('BBB/1.txt','w',encoding='utf-8')
# file.close()
#2.切换到指定BBB目录创建,默认的路径是py文件操作的目录
#查看操作目录的路径
# cur_path = os.getcwd()#py文件的目录
# print(cur_path)
# #切换到指定目录
# os.chdir('BBB')
# cur_path = os.getcwd()
# print(cur_path)
# file = open('2.txt','w',encoding='utf-8')
#既可以修改文件夹，又可以修改文件名
# os.renames("BBB/1.txt","CC/3.txt")
#查看目录下的文件名列表信息
# filename_list = os.listdir('CCC')
# print(filename_list)

# os.chdir('CC')
# cur_path = os.getcwd()
# print(cur_path)
# #os.listdir('.')表示当前目录，“.."表示上一级目录
# filename_list = os.listdir()
# print(filename_list)

#删除文件
# os.remove("CCC/3.txt")
#删除文件夹
# os.rmdir("CCC")
#rmdir只能删除空目录
#os.rmdir('CC')

#删除目录树
shutil.rmtree("CC")