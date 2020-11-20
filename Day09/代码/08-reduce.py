from functools import reduce

# reduce以前是一个内置函数
# 内置函数和内置类都在builtins.py文件里
#
# scores = [1, 2, 3, 4, 5]
#
# print(reduce(lambda ele1, ele2: ele1 * ele2, scores))   #120

# 用reduce求所有学生的总年龄
students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 25, "score": 93, "height": 170},
    {"name": "jerry", "age": 30, "score": 90, "height": 173},
    {"name": "kevin", "age": 30, "score": 90, "height": 176},
    {"name": "poter", "age": 27, "score": 88, "height": 170},

]

# def get_ages(x, y):
#     return x + y['age']
#  # 0相当于初始化的值
# print(reduce(get_ages, students, 0))
print(reduce(lambda x, y: x + y['age'], students, 0))
