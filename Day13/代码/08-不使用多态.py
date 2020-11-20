# 多态是基于继承,通过子类重写父类的方法,达到不同的子类对象调用相同的父类方法，得到不同的结果,提高代码的灵活度
class Police_Dog(object):
    def attact_enemy(self):
        print('警犬正在攻击坏人')

class Bind_Dog(object):
    def lead_road(self):
        print('导盲犬正在领路')

class Drug_Dog(object):
    def search_drug(self):
        print('缉毒犬正在搜索毒品')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.dog = None

    def workwith_pd(self):
        if self.dog is not None:
            self.dog.attact_enemy()

    def workwith_bd(self):
        if self.dog is not None:
            self.dog.lead_road()

    def workwith_dd(self):
        if self.dog is not None:
            self.dog.search_drug()


p = Person("张三")
pd = Police_Dog()
p.dog = pd
p.workwith_pd()

bd = Bind_Dog()
p.dog = bd
p.workwith_bd()

dd = Drug_Dog()
p.dog = dd
p.workwith_dd()
