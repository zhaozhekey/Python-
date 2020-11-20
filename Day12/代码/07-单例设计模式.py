class Singleton(object):
    __instance = None     #类属性
    __isFirst = True    #指定只有第一创建的时候才修改初始值

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)
        return cls.__instance
        # pass

    def __init__(self, a, b):
        if self.__isFirst:
            self.a = a
            self.b = b
            self.__isFirst = False

# 调用 __new__方法申请内存
# 如果不重写__new__方法，会调用object的__new__ 方法
# object的__new__方法会申请内存
# 如果重写了__new__方法，需要自己手动申请内存
s1 = Singleton("哈哈", "嘿嘿嘿")
s2 = Singleton("呵呵", "嘻嘻嘻")
print(hex(id(Singleton)))
print(s1)
print(s2)

print(s1 is s2)

print(s1.a)