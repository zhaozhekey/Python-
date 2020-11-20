# 多态是基于继承,通过子类重写父类的方法,达到不同的子类对象调用相同的父类方法，得到不同的结果,提高代码的灵活度
class Dog(object):
    def work(self):
        print("狗正在工作")


class Police_Dog(Dog):
    def work(self):
        print('警犬正在攻击坏人')


class Bind_Dog(Dog):
    def work(self):
        print('导盲犬正在领路')


class Drug_Dog(Dog):
    def work(self):
        print('缉毒犬正在搜索毒品')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work(self):
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


p = Person("张三")
pd = Police_Dog()
p.dog = pd
p.work()

bd = Bind_Dog()
p.dog = bd
p.work()

dd = Drug_Dog()
p.dog = dd
p.work()
