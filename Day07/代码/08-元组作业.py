# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
#   1) 求选课学生总共有多少人
#   2) 求只选了第一个学科的人的数量和对应的名字
#   3) 求只选了一门学科的学生的数量和对应的名字
#   4) 求只选了两门学科的学生的数量和对应的名字
#   5) 求选了三门学科的学生的数量和对应的名字

sing = ("李白", "白居易", "李清照", "杜甫", "王昌龄", "王维", "孟浩然", "王安石")
dance = ("李商隐", "杜甫", "李白", "白居易", "岑参", "王昌龄")
rap = ("李清照", "刘禹锡", "岑参", "王昌龄", "苏轼", "王维", "李白")

#   1)
#   自己的方法
first = []
count = 0
for person in sing:
    if person not in first:
        first.append(person)
        count += 1
for person in dance:
    if person not in first:
        first.append(person)
        count += 1
for person in rap:
    if person not in first:
        first.append(person)
        count += 1
print(first)
print(count)
print("----------------------")
# 老师的方法
first_teacher = sing + dance + rap
print(set(first_teacher))
print(len(set(first_teacher)))
print("=====================================================")

# 2)
second = []
for person in sing:
    if not (person in dance or person in rap):
        second.append(person)
print(second)
print(len(second))
print("=====================================================")

# 3)
third = list(sing + dance + rap)
third_person = {}
for person in third:
    # if person in third_person:
    #     third_person[person] += 1
    # else:
    #     third_person[person] = 1
    if person not in third_person:
        third_person[person] = third.count(person)
print(third_person)
count1 = 0
person1 = []
count2 = 0
person2 = []
count3 = 0
person3 = []
for key, value in third_person.items():
    if value == 1:
        count1 += 1
        person1.append(key)
    elif value == 2:
        count2 += 1
        person2.append(key)
    else:
        count3 += 1
        person3.append(key)
print("只选了一门学科的人有", count1, "人")
print("只选了一门学科的人是:", person1)
print("选了两门学科的人有", count2, "人")
print("选了两门学科的人是:", person2)
print("选了三门学科的人有", count3, "人")
print("选了三门学科的人是:", person3)

print("=====================================================")


