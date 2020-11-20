# 模块，在python里，一个py文件就可以理解为一个模块
#   不是所有的py文件都能作为模块进行导入
#  如果想让一个py文件能够被导入，模块名字必须遵守命名规则
#   Python为了方便我们开发，提供了很多内置模块


import time  # 方式一  使用import 模块名  直接导入一个模块
from random import randint  # 方式二   from  模块名  import  函数名，导入一个模块里的方法或者变量
from math import *  # 方式三    from 模块名 import * 导入这个模块里的“所有”方法和变量
import datetime as dt  # 方式四  import 模块名 as 别名  ， 导入一个模块并给这个模块起一个别名
from copy import deepcopy as dp  # 方式五   from 模块名 import 方法名 as 别名

# 导入这个模块之后，就可以使用这个模块里的方法和变量
print(time.time())  # 方式一

randint(0, 2)  # 方式二  生成[0,2]的随机整数
# random.randint(0,2)    使用方式二之后，直接使用函数即可，无需在写模块名，否则会报错

print(pi)  # 方式三

print(dt.MAXYEAR)  # 方式四

dp(['hello', 'hi', [100, 200, 300], 'world'])  # 方式五
