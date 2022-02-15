#了解即可

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

a=Car()
print(Car.brand)
Car.brand = '宝马'
print(Car.brand)
b=Car()
print(a.brand,b.brand) # a和b的brand都被修改了
a.color='黑色'
del Car.color
# print(Car.color) 
print(a.color) # 修改过后的color属于它自己的，所以还能得到
