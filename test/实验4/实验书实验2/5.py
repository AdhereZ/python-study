k=input('请输入一个key数组: ').split(',')
v=input('请输入一个value数组: ').split(',')

k=[int(k[i]) for i in range(len(k))]
v=[int(v[i]) for i in range(len(v))]

dict1=dict(zip(k,v))
print(dict1)