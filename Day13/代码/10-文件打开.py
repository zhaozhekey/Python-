# open 参数介绍
# file：用来指定打开的文件(不是文件的名字，而是文件的路径)
# mode，打开文件时的模式，默认是r  表示只读
# encoding：打开文件时的编码方式

# open函数会有一个返回值，打开的文件对象

# xxx.txt写入时，使用utf-8编码格式
# 在windows操作系统里，默认使用GBK编码格式打开文件
# 解决方法：写入和读取使用相同的编码格式
file = open('./xxx.txt',encoding='utf-8')
print(file.read())

file.close()    #操作完成之后，关闭文件