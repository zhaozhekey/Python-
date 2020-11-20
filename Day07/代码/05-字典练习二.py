# 输入用户姓名，如果姓名已经存在，提示用户；如果姓名不存在，继续输入年龄，并存入列表中

persons = [
    {"name": "zhangsan", "age": 18, "gender": "female"},
    {"name": "lisi", "age": 20, "gender": "male"},
    {"name": "jack", "age": 30, "gender": "unknow"},
    {"name": "kevin", "age": 29, "gender": "female"}
]

# name_input = input("请输入姓名")
#
# for person in persons:
#     if name_input == person['name']:
#         print("该姓名已经存在")
#         break
# else:
#     new_person = {'name': name_input}
#     age = int(input("请输入年龄"))
#     new_person['age'] = age
#     persons.append(new_person)
#
# print(persons)

#删除性别不明的人
new_person = [person for person in persons if person['gender'] != "unknow"]
print(new_person)
