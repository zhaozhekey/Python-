print(chr(77))
print(ord('c'))

x = "大家好，我是{}，我今年{}岁了".format("张三", 29)
print(x)

#{数字}  根据数字的顺序进行填入
y = "大家好，我是{1}，我今年{0}岁了".format(28,"jerry")
print(y)

#{变量名}，根据变量名进行填入
z = "我是{name},我的地址是{addr}".format(name = "lisi",addr = "重庆市渝中区人民路232号")
print(z)