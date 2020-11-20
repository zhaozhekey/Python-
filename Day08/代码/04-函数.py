# #返回值就是函数执行的结果，并不是所有的函数都必须要有返回值，如果一个函数没有返回值，那他的返回值就是None
#
# def add(a,b):
#     return a+b
# print(add(3,4))

def add(n, m):
    result = 0
    for i in range(n, m):
        result += i
    return result

print(add(-5, 0))
