d=dict(name='zjh',age=20,grade=19,height=180,weight=133)


#删除元素
a=d.pop('name')
print('被删除的元素的值',a)
print(d)

print('更新')
d.update({'age':30})
print(d)

print('添加')
d['sex']='男'
print(d)
