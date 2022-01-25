# 输入两个集合，输出他们的并集，交集，差集
a=input()

b=input()

a=(a)
b=eval(b)

x1=a&b
x2=a|b
x3=a-b

print('交集\n',x1)
print('并集\n',x2)
print('差集\n',x3)