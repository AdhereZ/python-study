# 成员方法中的self
# self在方法中代表的是对象自己
# self就可以在类内部代替对象进行各种操作

class Person():
  name='张三'
  sex='男'
  age='18'

  def sing(self):
    print(f'我{self.name}会唱歌')
  
  #类不能调用含有self的函数
  def func(self):
    print(self.dad)
    self.name='李四'
    self.height=180
    self.sing()
  
  # 不含self的函数只能类调用，对象无法调用，绑定类方法
  def func2():
    print('我只能让类调用')


zs=Person()
zs.dad='王二'
zs.sing()
zs.func()
print(zs.name,zs.height)
zs.func2()