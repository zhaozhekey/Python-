# Python中使用print内置函数来输出语句

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep参数用来表示输出时，每个值之间使用哪种字符作为分隔。默认使用空格作为分隔符。
# end的作用是当执行完一个print语句之后，接下来要输出的字符。默认是\n，表示换行
# file的作用是将输出内容输出到指定文件中
f = open('x.txt','w')
print('hello','hi','go','workhard',sep='_')
print('大家好，我是渣渣辉',end='，  ',file=f)
print('好好学习',file=f)

