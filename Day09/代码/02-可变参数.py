# *args 表示可变位置参数
# **kwargs 表示可变的关键字参数

def add(a, b, *args, mul=1, **kwargs):  # *args表示可变参数
    # print("a = {},b = {}".format(a, b))
    # print("args = {}".format(args))  # 多出来的可变参数会以元组的形式保存到args里
    c = a + b
    for arg in args:
        c += arg
    return c * mul


print(add(3, 1))
print(add(3, 6, 5, 1,))
print(add(5, 7, 3, 3, 6, 4, 3, 1, 6, 3, 5))

print(add(3, 6, 5, 1, mul=2, x=1, y=2))
