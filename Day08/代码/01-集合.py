#集合
#集合没有查询的方法

names = {'hello',1,"good","hello"}
print(names)    #{1, 'good', 'hello'}
#
# names.clear()  #清空set集合
# print(names)    #输出结果：set()

names.add("阿珂")
print(names)    #{'hello', '阿珂', 'good', 1}

names.pop() #随机删除一个
print(names)

names.remove("good")    #删除指定元素
print(names)

#union 将多个集合合并生成一个新的集合
print(names.union("亚瑟", "妲己"))  #{'阿珂', 1, '亚', '瑟', '妲', '己'}
print(names.union({"亚瑟", "妲己"}))    #{'妲己', '亚瑟', 'hello', '阿珂'}
print(names)    #{'hello', '阿珂'}

#A.update(B) 将B拼接到A里
names.update("甄姬", "嬴政")
print(names)    #{'嬴', '政', '甄', '阿珂', '姬', 'hello'}

names.update({"甄姬", "嬴政"})
print(names)    #{1, '嬴', '甄姬', '姬', '嬴政', '甄', 'hello', '政'}