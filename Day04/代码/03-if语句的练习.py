# 写出判断一个数是否能同时被3和7整除的条件语句，并且打印对应的结果
#
# num = int(input("请输入数字"))
# if (num%3 == 0 and num%7 == 0):
#     print("该数字能同时被3和7整除")
# else:
#     print("该数字不能同时被3和7整除")

# 假设今天上课的时间是15678秒，编程计算今天上课是多小小时，多少分钟，多少秒

time = 15678
hour  = time // 3600
minute = time % 3600 // 60
second = time % 60
print("共上课",hour,"小时",minute,"分钟",second,"秒")

age = int(input("请输入你的年龄"))

if age > 18:
    pass #使用pass进行占位，没有意义，单纯为了保证语句的完整性，使程序不报错。
print("hello")