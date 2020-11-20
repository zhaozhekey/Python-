import json
# eval是python里一个较为强大的内置函数，可以执行字符串里的代码
a = 'input("请输入用户名")'  # a是一个字符串
b = '1+1'
print(eval(b))  # 输出结果：2

# JSON的使用，把列表、元组、字典等被转换成为JSON字符串
person = {"name": "zhangsan", "age": 18, "gender": "male"}
#字典如果想要把它传给前端页面或者把字典写入到一个文件里
m = json.dumps(person)  #dumps将字典、列表、集合、元组等转换成为JSON字符串
print(m)    #输出结果：{"name": "zhangsan", "age": 18, "gender": "male"}
print(type(m))  #<class 'str'>


n = '{"name":"lisi","age":18,"gender":"female"}'

s = json.loads(n)   #loads可将json字符串转化为python里的数据类型
print(s)            #{'name': 'lisi', 'age': 18, 'gender': 'female'}
print(type(s))      #<class 'dict'>


#   Python                          JSON
#   True                            true
#   Flase                           false
#   字符串                          字符串
#   字典                            对象
#  列表、元组                        数组

















