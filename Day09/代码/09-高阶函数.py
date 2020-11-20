# 1. 一个函数作为另一个函数的返回值
def test():
    print("我是test函数")
    return 'hello'


def demo():
    print("我是demo函数")
    return test


def bar():
    print("我是bar函数")
    return test()


a = bar()
print(a)

x = test()
print(x)

y = demo()  # y 是test函数，相当于test函数的别名
print(y)
z = y()
print(z)  # 'hello'


# 2. 一个函数作为另一个函数的参数


# 3. 函数内部再定义一个函数

def outer():
    x = 10  # 在外部函数里定义了一个变量x,是一个局部变量

    def inner():
        #   在内部函数如何修改外部函数的局部变量
        nonlocal x  # 此时，这里的x不再是新增变量，而是外部的局部变量x
        y = x + 1
        print("y=", y)

    print("outer的x变量", x)

    return inner

outer()()
