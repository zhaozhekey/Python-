# 在python里，可以使用一对单引号、双引号或者一对三个双引号、一对三个单引号进行表示
a = 'hehe'
b = "good"
c = """呵呵呵"""
d = '''嘿嘿嘿'''

word = "goodmorning"
print(word[4])

m = 'abcdefghijklmnopqrstuvwxyz'
print(m[5])  # m[index] ==> 获取指定下标上的数据
# 切片  m[start:end:step]     step指的是步长，理解为间隔。
print(m[2: 9])  # cdefghi    包左不包右   包含start不包含step
print(m[2:])  # cdefghijklmnopqrstuvwxyz   从start开始全部“截取”
print(m[:9])    #abcdefghi  从开始截取到end结束 不包含end
print(m[2:9:3])  # cfilorux  从start开始 到end结束 ，每见隔（step-1）个字符截取一次  步长不能为0
print(m[3:15:1])    #  输出结果 defghijklmno
print("------------")
print(m[3:15:-1])   #  输出结果
print("-----------")
print(m[15:3])      #  输出结果
print("-----------")
print(m[15:3:-1])   #  输出结果 ponmlkjihgfe

#start和end如果为负数，表示从右获取
print(m[-5:-9])       #  输出结果
print("------------")
print(m[-9:-5])       #  输出结果   rstu

str = "abcdefghijklmnllkjhdsfg"
#查找内容：find，index，rfind，rindex
print(str.find("l"))    #11
print(str.index("l"))   #11

print(str.find("p"))    #-1 如果字符不存在，结果是-1
# print(str.index("p"))   #报错，使用index，如果字符不存在，会报错

print(str.rfind("l"))   #找最大的索引

print("hello".isalpha())    #判断是不是字母
print("hello".isdigit())    #判断是不是数字
print("hello".isalnum())    #判断是否由数字和字母组成

#replace方法用来替换字符串

word = "hello"
print(word.replace("l", "m"))  #hemmo   原来的字符串不会改变，而是生成一个新的字符串来保存替换后的结果
print(word) #hello  字符串是不可变数据类型

x = "zhangsan-lisi-wangwu-jerry-tony"
#使用split方法，将字符串切割成一个列表
print(x.split('-'))     #输出结果：['zhangsan', 'lisi', 'wangwu', 'jerry', 'tony']
print(x.rsplit('-'))    #输出结果：['zhangsan', 'lisi', 'wangwu', 'jerry', 'tony']

print('--------------')

print(x.split('-', 2))      #输出结果：['zhangsan', 'lisi', 'wangwu-jerry-tony']
print(x.rsplit('-', 2))     #输出结果：['zhangsan-lisi-wangwu', 'jerry', 'tony']

# partition 指定一个字符串作为分隔符，分为三部分
print('abvsdfXsldjXsldkj'.partition('X'))   #输出结果：('abvsdf', 'X', 'sldjXsldkj')
print('abvsdfXsldjXsldkj'.rpartition('X'))  #输出结果：('abvsdfXsldj', 'X', 'sldkj')





























