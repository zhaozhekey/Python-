# uuid用来生成一个全局唯一的id模块
import uuid

print(uuid.uuid1())
print(type(uuid.uuid4()))
x = str(uuid.uuid4())
print(x)
print(x.replace("-", ""))
