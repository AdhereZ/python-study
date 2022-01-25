# 数组的解包
""" a=[1,2,3,4,5]
c,*d,b=a
print(c)
print(d)
print(b) """

# 元组的解包
""" (a,b),(c,d)=(1,2),(3,4)
print(a,b,c,d,sep=',') """

# 字典的解包
a={'age':20,'name':'zjh','sex':'male'}
b,c,d=a
print(b,c,d,sep=' ')
b,c,d=a.values()
print(b,c,d,sep=' ')

