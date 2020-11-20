# 删除性别不明的人

persons = [
    {"name": "Kevin", "age": 18, "gender": "female", "score": 98},
    {"name": "lisi", "age": 20, "gender": "unknown", "score": 88},
    {"name": "jack", "age": 30, "gender": "unknown", "score": 84},
    {"name": "jerry", "age": 30, "gender": "female", "score": 90},
    {"name": "jason", "age": 30, "gender": "unknown", "score": 88},
    {"name": "王五", "age": 30, "gender": "female", "score": 78},
    {"name": "zhangsan", "age": 29, "gender": "unknown", "score": 88}
]

# # 方法一  使用推导式,将不需要的数据添加到新列表中
# new_persons = [person for person in persons if person["gender"] != "unknown"]
# print(new_persons)
#
# # 方法二    使用for循环  使用for循环倒着删除要删除的数据，避免“坑”
# i = 0
# for i in range(len(persons) - 1, -1, -1):
#     if persons[i]["gender"] == "unknown":
#         persons.remove(persons[i])
# print(persons)
#
# # 方法三    使用while循环  使用while循环删除需要删除的数据，并及时补齐因删除数据而导致的列表数据索引变化，避免漏删数据
# j = 0
# while j < len(persons):
#     if persons[j]["gender"] == "unknown":
#         persons.remove(persons[j])
#         j -= 1
#     j += 1
# print(persons)
#
# # 方法四    使用浅复制  遍历在新的列表中操作，删除是在原来的列表中操作
# #   (persons[:]是对persons的切片操作，所以删除原persons的数据对切片无影响)
# for person in persons[:]:
#     if person["gender"] == "unknown":
#         persons.remove(person)
# print(persons)
#
# # 方法五    使用filter内置函数
# new_persons5 = filter(lambda x: x['gender'] != 'unknown', persons)
# print(list(new_persons5))

