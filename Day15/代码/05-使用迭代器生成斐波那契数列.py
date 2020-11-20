import time

class Fibonacci(object):
    def __init__(self, x):
        self.x = x
        self.num1 = 1
        self.num2 = 1
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.x:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.count += 1
            # time.sleep(1)
            return x
        else:
            raise StopIteration


f = Fibonacci(3000)
for i in f:
    print(i)
