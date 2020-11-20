# import math
#
# while True:
#     age = float(input("请输入你的年龄："))
#     # if 150 > age >= 0:
#     #     # if 18 > age >= 0:
#     #     #     print("未成年")
#     #     # else:
#     #     #     print("已成年")
#     #     print("未成年") if age < 18 else print("已成年")
#     # else:
#     #     print("这家伙不是人")
#
#     print("这家伙不是人") if age > 150 or age < 0 else print("未成年") if age < 18 else print("已成年")
#
# for i in range(0, 101):
#     if i % 2 != 0:
#         print(i,end=" ")
#
#
# # 统计100以内，个位数是2，且能被3整除的个数
# num = 0
# for i in range(1, 101):
#     if i % 10 == 2 and i % 3 == 0:
#         num += 1
#         print(i,end="\t")
# print(num)
#
#
# # 输入一个正整数，求它是几位数
# num = int(input("输入正整数"))
#
# while True:
#     if num > 0:
#         break
#     else:
#         num = int(input("输入正整数"))
# i = 0
# while True:
#     count = num // (10 ** i)
#     if count == 0:
#         print("该正整数是", i, "位数")
#         break
#     i += 1
#
#
# # 打印所有的水仙花数
# # 水仙花数是一个三位数，其各位数字立方和等于该数本身
# for num in range(100, 1000):
#     x = num % 10    #个位
#     y = (num // 10) % 10    #十位   y = num % 100 // 10
#     z = (num // 100) % 10   #百位   z = num // 100
#     sum = x ** 3 + y ** 3 + z ** 3
#     if sum == num:
#         print(num)
#
# while True:
#     num = int(input("请输入数字"))
#     if num == 0:
#         print("程序结束")
#         break
#
#
# # 使用for...else语句写素数
# for num in range(2, 20):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, "是素数")
#
# # 统计101-200中素数的个数
# count = 0
# for num in range(101, 201):
#     i = 2
#     flag = False
#     while i <= num / 2:
#         if num % i == 0:
#             flag = True
#             break
#         i += 1
#     if flag == False:
#         count += 1
#         print(num)
# print("个数", count)
#
#
# # 打印斐波那契数列
# #  1  1  2  3  5  8  13  21  34  55  89  144  233
# while True:
#     count = int(input("请输入个数"))
#     num1 = 1
#     num2 = 1
#     # if count < 2:
#     #     print("第",count,"个数是",num1)
#     # else:
#     for i in range(2,count):
#         temp = num1
#         num1 = num2
#         num2 = temp +num2
#     print("第",count,"个数是",num2)
#
#
# #  "百马百担"问题：一匹大马能驮3担货，一匹中马能驮2担货，两匹小马能驮1担货，
# #  如果用一百匹马驮一百担货，问有大、中、小马各几匹？
#
# for da in range(0, 40):
#     for zhong in range(0, 50):
#         for xiao in range(0, 100):
#             if xiao % 2 == 0:
#                 if (da * 3 + zhong * 2 + xiao / 2 == 100) and (da + zhong + xiao == 100):
#                     print("大马：", da, "中马：", zhong, "小马：", xiao)
#
# for x in range(0, 100 // 3 + 1):
#     for y in range(0, 100 // 2 + 1):
#         if x * 3 + y * 2 + (100 - x - y) * 0.5 == 100:
#             print("大马：", x, "中马：", y, "小马：", 100 - x - y)
#
#
# # 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度(8848.13m)？
#
# count = 1
# while True:
#     num = 0.00008 * (2 ** count)
#     if num > 8848.130:
#         print("对折", count, "次之后能达到珠穆朗玛峰的高度(8848.13m)")
#         break
#     count += 1
