""" 
魔术方法：
  魔术方法和普通方法都是类中定义的方法
  不需要手动调用，在某种情况下自动触发
  大多数魔术方法前后都有两个连续的下划线
  魔术方法是系统定义好的，我们来使用 
"""

""" 
__init__ 初始化方法
 在类实例化对象后，自动触发
 """

class Person():
  name=None
  age=None
  sex=None

  def __init__(self,name,age,sex):
      print('我是实例化对象')
      self.name=name
      self.age=age
      self.sex=sex
      self.say()

  def say(self):
    print(f'我的名字是{self.name},我的年龄是{self.age},我的性别是{self.sex}')

zs=Person('张三',18,'男')

