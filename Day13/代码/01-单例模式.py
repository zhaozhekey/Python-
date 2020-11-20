class Singleton(object):
    __instance = None
    __isFirst = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__isFirst:
            self.a = a
            self.b = b
            self.__isFirst = False


s1 = Singleton("哈哈", "嘿嘿嘿")
s2 = Singleton("呵呵", "嘻嘻嘻")

print(s1.a)
print(s2.a)

print(s1 is s2)
