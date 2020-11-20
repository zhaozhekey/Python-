# i = 0
# while i < 5:
#     i += 1
#     print("*" * i)

# 循环嵌套打印矩阵
j = 0
while j < 10:
    j += 1
    i = 0
    while i < 5:
        i += 1
        print("*", end="  ")
    print()


#循环嵌套打印三角形
i = 0
while i < 10:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("*", end=" ")
    print()

# 打印九九乘法表
j = 1
while j < 10:
    i = 1
    while i <= j:
        print(i, "*", j, "=", i * j,sep="", end="\t")
        i += 1
    j += 1
    print()
