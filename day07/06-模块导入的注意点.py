# -*- coding:utf-8 -*-
#模块导入的注意点
#1.自定义的模块名不要和系统的模块名重名
#2.导入的功能代码不要在当前模块定义否则使用不了导入模块的功能代码
import sys
#查看模块搜索的顺序
print(sys.path)