#创建字典
keys=['a','c','f','zjh']
values=[1,2,3,4]
dic=dict(zip(keys,values))
print(dic,'\n')

d=dict(name='zjh',age=20,grade=19,height=180,weight=133)
print(d,'\n')

adict=dict.fromkeys(['name','age','sex'])
print(adict,'\n')

print(d.keys())
print(d.values())
print(d.items())
print()

for key,value in d.items():
   print(key,value,sep=':')
