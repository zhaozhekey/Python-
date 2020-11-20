#
# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i,end="")
#     i += 1


username = input("用户名")
password = input("密码")
while (username !="zz" or password != "123"):
# while not(username =="zz" or password == "123"):
    username = input("用户名")
    password = input("密码")