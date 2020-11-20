# 魔法方法也叫魔术方法，是类里的特殊方法
# 特点
# 1.无需手动调用，会在合适的时机自动调用
# 2.这些方法，都是使用__开始，使用__结束
# 3.方法名都是系统规定好的，在何时的时机自己调用


class Person(object):
    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print("__init__方法被调用了")
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print("__del__方法被调用了")

    def __repr__(self):
        return "hello"

    def __str__(self):
        # return "good"
        return "姓名是{}，年龄是{}".format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print("__call__方法被调用了")
        #args 是一个元组，保存(1,2)
        # kwargs 是一个字典  {'fn': <function <lambda> at 0x000001B3F9F48708>}
        print("args = {},kwargs = {}".format(args,kwargs))
        x = args[0]
        y = args[1]
        test = kwargs['fn']
        return test(x,y)


p = Person("张三", 18)

# 如果不做任何的修改，直接打印一个对象，是文件的__name.__类型   内存地址
# print(p)    #<__main__.Person object at 0x0000017E6CF3BE48>

# 当打印一个对象的时候，会调用这个对象的__str__ 或者__repr__方法
# 如果两个方法都写了，选择__str__方法
# 使用__str__和__repr__方法，都会修改一个对象转换成字符串的结果。一般来说，__str__方法的结果
# 更加在意可读性，而__repr__方法的结果更加在意正确性
print(p)  # good

print(repr(p))  # 调用内置函数repr 会触发对象的__repr__方法
print(p.__repr__())  # 魔法方法，一般不会手动调用

# 如果定义类的时候没有定义 __call__方法，调用p()时会报错  TypeError: 'Person' object is not callable
# p() #对象名()==> 调用这个对象的__call__方法，还可以进行传参，传参如下：

x = p(1, 2, fn=lambda x, y: x + y)
print(x)