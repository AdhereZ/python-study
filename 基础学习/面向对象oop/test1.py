class Car():
  #属性
  color = '白色'
  brand = '奥迪'
  pailiang = 2.4
  
  # 方法
  def lahuo(self):
    print('拉货')
  
  def doufeng(self):
    print('兜风')


c=Car()
b=Car()
a=Car()

""" b.color='黑色' # 实际上等于给这个对象创建了一个a对象自己的color属性
c.name='aodi'
print(c.color)
print(b.color)
print(c.name)
# del b.brand # 这里brand不能删除
del c.name # 这里name可以删除 因为name就是属于实例c的，所以可以删除时
print(c.name) """

a.lahuo()
def func():
  print('new func')
a.lahuo=func
a.lahuo()

a.func2=func
a.func2()
del a.func2 # 可以删除
a.func2()

del a.doufeng # 不能删除

