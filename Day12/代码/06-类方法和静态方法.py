class Person(object):
    type = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):    #对象方法有一个参数self，指的是实例对象
        print(self.name,"正在吃",food)

    #如果一个方法里没有用到实例对象的任何属性，可以将这个方法定义成static
    @staticmethod
    def demo():
        print("hello")

    @classmethod
    def test(cls):  #如果这个函数只用到了类属性，我们可以把函数定义成为一个类方法
        # 类方法会有一个参数cls，也不需要手动的传参，会自动传参
        # cls指的是类对象   cls is Person
        print(cls.type)
        print("yes")


p1 = Person("张三", 18)
# 实例对象在调用方法时，不需要给形参self传参，会自动的把实例对象传递给self

p2 = Person("李四", 20)
# p1.eat("红烧牛肉面")
# Person.eat(p2,"西红柿")

#静态方法没有用到实例对象的任何属性
Person.demo()

# 类方法可以实例对象和类对象调用
p1.test()
Person.test()
