# 编写一个函数，求多个数中的最大值
def get_max(*args):
    x = args[0]
    for i in range(0, len(args)):
        if x < args[i]:
            x = args[i]
    return x


# 编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
import random


def get_sum(num):
    result = 0
    for i in range(1, num + 1):
        x = random.randint(1, 7)
        # print("第{}个骰子是{}".format(i, x))
        result += x
    return result


# 编写一个函数，交换指定字典的key和value
# 例如: dict1 = {'a':1, 'b':2, 'c':3} ==> dict1 = {1:'a', 2:'b', 3:'c'}
dict1 = {'a': 1, 'b': 2, 'c': 3}


def get_exchange(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict


# 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串
def get_alphas(words):
    new_words = ''
    for w in words:
        if w.isalpha():
            new_words += w
    return new_words


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 写一个函数，求多个数的平均值
def get_average(*args):
    x = 0
    for i in range(0, len(args)):
        x += args[i]
    return x / len(args)


# 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
def my_capitalize(words):
    new_words = ""
    new_words += words[0].upper()
    new_words += words[1:]
    return new_words


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束
def my_endswith(words, ele):
    return words[-len(ele)::] == ele


# 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_digit(words):
    for w in words:
        if not ('0' <= w <= '9'):
            return False
    return True


# 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母
def my_upper(words):
    new_words = ''
    for word in words:
        if 'a' <= word <= 'z':
            new_word = chr(ord(word) - 32)
            new_words += new_word
        else:
            new_words += word
    return new_words


# 写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在
def my_in(it, ele):
    for item in it:
        if item == ele:
            return True
    return False


# 写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串
# print(my_replace('how you and you fine you ok', 'you', 'me'))
def my_replace(str, old, new):
    new_str = ""
    i = 0
    while i <= len(str) - 1:
        if str[i:len(old) + i] == old:
            new_str += new
            i += len(old)
        else:
            new_str += str[i]
            i += 1
    return new_str


# #老师方法一
# def my_replace(all_str, old_str, new_str):
#     result = ''
#     i = 0
#     while i < len(all_str):
#         temp = all_str[i:i + len(old_str)]
#         if temp != old_str:
#             result += all_str[i]
#             i += 1
#         else:
#             result += new_str
#             i += len(old_str)
#     return result

# # #老师方法二
# def my_replace(all_str, old_str, new_str):
#     return new_str.join(all_str.split(old_str))



# 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典值的最大值
def get_max2(seq):
    if isinstance(seq, dict):
        seq = list(seq.values())
    x = seq[0]
    for i in range(0,len(seq)):
        if x < seq[i]:
            x = seq[i]
    return x


print(get_max(1, 9, 6, 3, 4, 5))
print(get_sum(5))
print(get_exchange(dict1))
print(get_alphas('hello123good456'))
print(get_factorial())
print(get_average(1, 2, 3, 4, 5, 6))
print(my_capitalize('hello'))
print(my_capitalize('34hello'))
print(my_endswith('hello', 'llo'))
print(my_digit('12390aa'))
print(my_upper('hel34lo'))
print(my_in(['zhangsan', 'lisi', 'wangwu'], 'jack'))
print(my_in({'name': 'zhangsan', 'age': '18'}, 'name'))
print(my_replace('how youou and you fine you ok', 'you', 'asdfg'))
# ['zhangsan','lisi','wangwu']  ==> zhangsan_lisi_wangwu

print(get_max2([2, 4, 8, 1, 9, 0, 7, 5]))
print(get_max2({'x': 10, 'y': 29, 'z': 32, 'a': 23, 'b': 19, 'c': 98}))
