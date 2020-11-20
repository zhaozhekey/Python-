# 将列表按照学生成绩从大到小排序

persons = [
    {"name": "Kevin", "age": 18, "gender": "female", "score": 98},
    {"name": "lisi", "age": 20, "gender": "unknown", "score": 88},
    {"name": "jack", "age": 30, "gender": "unknown", "score": 84},
    {"name": "jerry", "age": 30, "gender": "female", "score": 90},
    {"name": "jason", "age": 30, "gender": "unknown", "score": 88},
    {"name": "王五", "age": 30, "gender": "female", "score": 78},
    {"name": "zhangsan", "age": 29, "gender": "unknown", "score": 88}
]
# 方法一
# i = 0
# score = []
# j = 0
# while i < len(persons):
#     score.append(persons[i]["score"])
#     i += 1
# score.sort()
# print(score)
#
# new_person = []
# while j < len(score):
#     for person in persons:
#         if score[j] == person["score"] and person not in new_person:
#             new_person.append(person)
#             j += 1
#             break
# print(new_person)

# 方法二
for j in range(0, len(persons) - 1):
    for i in range(0, len(persons) - 1):
        if persons[i]["score"] > persons[i + 1]["score"]:
            persons[i], persons[i + 1] = persons[i + 1], persons[i]
print(persons)
