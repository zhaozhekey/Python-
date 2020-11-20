import copy
#深复制只能使用copy模块
words = ['hello', 'world', '', [100, 200, 300], 'yes', 'ok']

words1 = words.copy()
words2 = copy.deepcopy(words)
print("words1:",words1)     #['hello', 'world', '', [100, 200, 300], 'yes', 'ok']
print("words2:",words2)     #['hello', 'world', '', [100, 200, 300], 'yes', 'ok']

words[0] = "你好"
print("words1:",words1)     #['hello', 'world', '', [100, 200, 300], 'yes', 'ok']
print("words2:",words2)     #['hello', 'world', '', [100, 200, 300], 'yes', 'ok']

words[3][0] = 1
print("words:",words)       #['你好', 'world', '', [1, 200, 300], 'yes', 'ok']
print("words1:",words1)     #['hello', 'world', '', [1, 200, 300], 'yes', 'ok']
print("words2:",words2)     #['hello', 'world', '', [100, 200, 300], 'yes', 'ok']