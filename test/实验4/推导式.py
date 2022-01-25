# 生成器推导式
g=((i+1)**2 for i in range(10))
print('生成器推导式\n',list(g))

# 字典推导式
a={str(i):i for i in range(1,5)}
print('字典推导式\n',a)

# 集合推导式
import random
a={random.randint(1,500) for i in range(100)}
print('集合推导式')
print(a)
print(len(a))
