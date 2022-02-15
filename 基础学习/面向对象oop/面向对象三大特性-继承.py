# 子类继承父类后，就可以去使用父类中的成员属性和方法（除了私有成员）

class maoke():
  maose='猫纹'
  sex='m'

  def ss(self):
    print('能上树')

  def jump(self):
    print('起跳')

class cat(maoke):
  sex='g'
  
  def ss(self):
    print('ss')

  def go(self):
    super().ss() #super调用父类的方法
    print(super().sex)  
c=cat()
c.jump()
print(c.maose)
print(c.sex)
c.ss()
c.go()
