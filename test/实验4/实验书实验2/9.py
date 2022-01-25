from functools import reduce
a=eval(input('输入包含若干集合的列表\n'))
print(reduce(lambda x,y:x|y,a))
