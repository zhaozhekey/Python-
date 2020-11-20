#os全称  OperationSystem操作系统
# os模块里提供的方法就是用来调用操作系统里的方法

import os

#os.name    获取操作系统的名称
print(os.name)  #windows系列==》nt，非Windows系列==》posix
print(os.sep)   #路径的分隔符
print(os.path.abspath('02-装饰器.py'))     #获取文件的绝对路径

