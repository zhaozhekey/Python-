import time


# def calc_time(fn):
#     print("我已经执行")
#
#     def inner():
#         start = time.time()
#         s = fn()
#         end = time.time()
#         print("总共用时", (end - start), "秒")
#         return s
#
#     return inner
#
#
# @calc_time  # 第一件事情调用cal_time，第二件事情把被装饰的函数传递给fn
# def get_sum():
#     x = 0
#     for i in range(1, 1000000):
#         x += i
#     # print("和是", x)
#     return x
#
#
# # 第三件事，当再次调用get_sum函数时，此时的get_sum函数已经不再是定义的get_sum函数，而是calc的返回值inner
# print("装饰后的demo = {}".format(get_sum))  # 装饰后的demo = <function calc_time.<locals>.inner at 0x000001EB481EFF78>
# m = get_sum()  # 运用装饰器后，不能这样直接获取函数的返回值，因为此时的get_sum已经是inner了，需要在inner中添加返回值
# print("m的值是", m)


def calc_time(fn):
    print("我已经执行")

    def inner(x):
    # def inner(x, *args, **kwargs)   该处可用可变参数进行参数的接收
        start = time.time()
        s = fn(x)
        end = time.time()
        # print("总共用时", (end - start), "秒")
        return s, end

    return inner


@calc_time  # 第一件事情调用cal_time，第二件事情把被装饰的函数传递给fn
def get_sum(num):
    x = 0
    for i in range(1, num):
        x += i
    # print("和是", x)
    return x


print("装饰后的demo = {}".format(get_sum))  # 装饰后的demo = <function calc_time.<locals>.inner at 0x000001EB481EFF78>
m = get_sum(10000000)
print("m的值是", m)
