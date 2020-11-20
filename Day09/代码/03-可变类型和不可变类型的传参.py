def test(a):
    a = 100


def demo(b):
    b[0] = 100


x = 1
test(x)
print(x)

y = [6, 4, 13, 52]
demo(y)
print(y)

