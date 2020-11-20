# 递归简单来说，就是函数内部自己调用自己
# 递归最重要的就是找到出口（停止的条件）

# 用递归做求1~n的和

# 自己的笨办法
count = 0
i = 1

def add(n):
    global count
    global i
    count += i
    i += 1
    if i <= n:
        add(n)
    return count

print(add(100))

#老师方法

def get_sum(n):
    if(n == 1):
        return 1
    else:
        return get_sum(n-1) + n

print(get_sum(100))


#联系 使用递归求 n!

def get_jc(n):
    if n == 1:
        return 1
    else:
        return get_jc(n-1) * n

print(get_jc(4))

#斐波那契数列

def get_fb(n):
    if n < 3:
        return 1
    else:
        return get_fb(n-1) + get_fb(n-2)

print(get_fb(8))

x = (5, 7, lambda x, y: x + y)
print(x)