students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 25, "score": 93, "height": 170},
    {"name": "jerry", "age": 30, "score": 90, "height": 173},
    {"name": "kevin", "age": 30, "score": 90, "height": 176},
    {"name": "poter", "age": 27, "score": 88, "height": 170},

]

# # 字典和字典之间不能进行比较运算，缺少比较规则
# students.sort()     #直接报错
# print(students)

# # 可行的方法
# def foo(ele):
#     return ele['age']   #通过返回值告诉sort方法，按照元素的哪个属性进行排序
#
# # 需要传递参数key 指定比较规则
# # key需要的是一个函数,即key的参数类型是个函数
# # 在sort内部实现的时候，调用了foo方法，并且传入了一个参数，参数就是列表里的元素
# students.sort(key = foo)
# print(students)

# 简便上述方法，使用lambda表达式
students.sort(key=lambda ele: ele['age'])
print(students)
