# 操作列表 增删改查

heros = ['妲己', '后羿', '王昭君', '亚瑟', '韩信', "后羿"]
heros1 = ['嬴政', '程咬金', '阿珂', '孙尚香', '庄周']

# 添加元素的方法  append insert  extend
heros.append("黄忠")  # 在列表的最后面追加一个元素
print(heros)

# insert(index,object) 需要两个参数
# index 表示下标，在哪个位置插入数据
# object 表示对象，具体插入哪个数据
heros.insert(2, "甄姬")
print(heros)

# extend(iterable)  需要一个可迭代对象
heros.extend(heros1)
print(heros)

print(heros.pop(3))
print(heros)

heros.remove('亚瑟')
print(heros)

# heros.clear()
# print(heros1)

# 查询相关的方法
print(heros.index("妲己"))

print(heros.count("后羿"))

print('王昭君' in heros)

print('甄姬' in heros)

print(heros)
heros[3] = '盲僧'
print(heros)

a = 20
b = 13

# a = a + b
# b = a - b
# a = a - b
# a = a ^ b
# b = a ^ b
# a = a ^ b


a, b = b, a
print(a)
print(b)
