#
# num = 0
# sum = 0
# while num <= 100:
#     if num %2 != 0:
#         sum += num
#     num += 1
# print(sum)


# 内置类range用于生成制定区间的整数序列
# 注意：in的后面必须是一个可迭代对象！！！
# 目前接触的可迭代对象： 字符串、列表、字典、元组、集合、range
# for num in range(0,5):
#     print(num)

sum = 0
for num in range(1,101):
    sum += num
print(sum)