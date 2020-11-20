import time     #time模块可获取当前的时间


def calc_time(fn):
    start = time.time()     #time模块里的time方法，可以获取当前时间的时间戳
    fn()
    end = time.time()
    print("总共用时", (end - start), "秒")


def demo():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)


calc_time(demo)
