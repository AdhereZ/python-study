# 字典的读取
d=dict(name='zjh',age=20,grade=19,height=180,weight=133)

print(d.keys())
print(d.values())
print(d.items())
print()

print('年龄：',d.get('age'))

for key,value in d.items():
   print(key,value,sep=':')