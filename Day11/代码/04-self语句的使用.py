class Student:
    # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性
    __slots__ = ('name', 'age', 'city')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print("大家好，我是", self.name)


# Student("张三", 20)这段代码具体做了什么？
# 1.调用__new__方法，用来申请内存空间
# 2.调用__init__方法传入参数，将self指向创建好的内存空间，填充数据
# 3.变量s1也指向创建好的内存空间
s1 = Student("张三", 20)
s1.say_hello()

# Student没有height会报错
# print(s1.height)

# 在没有定义slots属性的情况下，直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 动态属性  若slots属性进行了定义，该属性不在slots的定义范围内，则不能进行添加操作，会报错
s1.city = "上海"
print(s1.city)
s2 = Student("Kevin", 30)
s2.say_hello()
print(s2.age)
