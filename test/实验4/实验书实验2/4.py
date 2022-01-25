a=input('输入一个列表\n').split(',')
a1=[int(a[i]) for i in range(len(a))]
print(list(filter(lambda x:x%2==0,a1)))