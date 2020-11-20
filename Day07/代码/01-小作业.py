import random

# 有一个列表names，保存了一组姓名names=['zhangsan','lisi','chris','jerry','henry']
# 再让用户输入一个姓名，如果这个姓名再列表里存在，提示用户姓名已存在
# 如果这个姓名再列表里面不存在，就将这个姓名添加到列表里

names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
# 方法一：
# while True:
#     name = input("请输入一个姓名")
#     for i in range (0,len(names)):
#         if name == names[i]:
#             print("用户名已存在")
#             break
#     else:
#         names.append(name)
#     print(names)
# 方法二
# name = input("请输入一个姓名")
# if name in names:
#     print("用户名已存在")
# else:
#     names.append(name)
# print(names)

# 求列表里面的最大数
# nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# nums.sort()
# print(nums[len(nums) - 1])

# num = nums[0]
# for i in range(0, len(nums)-1):
#     if num < nums[i]:
#         num, nums[i] = nums[i], num
# print(num)

# 练习，删掉列表里面的空字符串
# words = ["hello","yes","","","no","ok",""]
#
# i=0
# while i< len(words):
#     if words[i] == "":
#         words.remove(words[i])
#         continue
#     i+=1
# print(words)


# 练习  一个学校，有3个办公室，现在有8个老师等待工位的分配，请编写程序，完成随机分配
teachers = ["teacher1", "teacher2", "teacher3", "teacher4", "teacher5", "teacher6", "teacher7", "teacher8"]
offices = [[], [], []]
# for teacher in teachers:
#     #方法一
#     # r = random.randint(0, 2)
#     # offices[r].append(teacher)
#     #方法二
#     office = random.choice(offices)
#     office.append(teacher)
# print(offices)


