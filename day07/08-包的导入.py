# -*- coding:utf-8 -*-
import first_package.first#推荐
import first_package.second

#使用包模块里面的代码
first_package.first.show_msg()
first_package.second.show_msg()

#import导入包里面设置别名
import first_package.first as one
one.show_msg()


# from 包名.模块名 import *

#注意：如果外界使用from包名import * 不会导入包里面的所有模块，需要使用——all——指定
