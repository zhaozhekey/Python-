# # person = {"name":"zhangsan","age":"18","height":"175"}
# # print(person.get("gender","female"))
# # print(person)
#
#
# nums1 = [1, 2, 34, 4]
# nums2 = [4, 7, 32, 5, 8]
# nums1.extend(nums2)
# print(nums1)    #[1, 2, 34, 4, 4, 7, 32, 5, 8]
#
#
# person1 = {"name":"zhangsan","age":18}
# person2 = {"addr":"重庆"}
# person1.update(person2)
# print(person1)      #{'name': 'zhangsan', 'age': 18, 'addr': '重庆'}

# 字典的遍历
# person = {"name": "zhangsan", "age": 18, "height": "180cm", "addr": "重庆"}
#
# #第一种
# for key in person:
#     print(key,":",person[key])
#
# #第二种
# for key in person.keys():
#     print(key,"=",person[key])
#
# #第三种方式：获取到所有的value
# #只能拿到值，不能拿到key
# for value in person.values():
#     print(value)
#
# #第四种
# # print(person.items())   #dict_items([('name', 'zhangsan'), ('age', 18), ('height', '180cm'), ('addr', '重庆')])
# #列表里的元素是元组，把元组当做整体进行遍历
# for item in person.items():
#     print(item[0],"是",item[1])
#
# #第五种
# for key,value in person.items():
#     print(key,"——",value)

# 练习  统计列表中出现次数最多的元素
chars = ['a', 'd', 'h', 'k', 'h', 'd', 'a', 'g', 's', 'e', 'g', 'd', 'h', 'a', 'h', 'h']
char_count = {}

for char in chars:
    # #方法一
    # if char in char_count:
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    # 方法二
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)

vs = char_count.values()
max = max(vs)
for key, value in char_count.items():
    if value == max:
        print(key, ":", value)


