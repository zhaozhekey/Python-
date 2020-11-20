# #
# #
# # # age = input("请输入你的年龄")
# # # age = int(age)
# # # print(age + 1)
# # #
# # # print(bool(None))
# # # # print(bool(none))
# # # print(bool('none'))
# # #
# # # print(bool([]))  #False
# # #
# # # if 3:
# # #     print("good")
# # #
# # # print(6/2)
# # # print(10/3)
# #
# #
# # print(3 ** 3)
# #
# # print(5 ** -1)
# #
# # print(27 ** (1/3))
# #
# # print("hello" + "world" + "i" + "love" + "you")
# #
# #
# # a,*b,c = 1,2,3,4,5,6
# # print(a,b,c)
# #
# # print('a' > 'e')
#
#
# 4 > 3 or print("哈哈哈")
# 4 < 3 or print("嘿嘿嘿")
#
#
# print(3 and 5 and 0 and "hello")
# print("good" and "yes" and "hell" and 100)
#
# print(0 or "" or "lisi" or ())
# print(0 or "" or set() or [])
# print(bin(23))
# print(bin(15))
#
# print(bin(23&15))
#
# print(5<<2)
# print(5<<3)
# print(5<<4)
# print(5<<5)


a = 0xF0384E
b = a>>16
print(b)
c = (a-(b<<16))>>8
print(c)
d = a-(b<<16)-(c<<8)
print(d)