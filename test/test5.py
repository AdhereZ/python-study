from functools import reduce
a = [i for i in range(1,21)]
print(a)
b = reduce(lambda x,y: x*y, a)
print(b)


