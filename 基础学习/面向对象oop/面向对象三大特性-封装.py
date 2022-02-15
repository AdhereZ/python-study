""" 
封装的级别

             共有的 public    受保护的 protected    私有的 private
在类的内部       OK                   OK                 OK
在类的外部       OK                   NO(python可以)     No

"""

class Person():
  name='名字'
  _age='年龄' #一个下划线是受保护属性
  __sex='性别'  #两个下划线是私有属性

  def __init__(self,n,a,s):
      self.name=n
      self._age=a
      self.__sex=s

  def say(self):
    print('聊天')

  def __sing(self):
    print('唱歌')

  def kiss(self):
    print('kiss')

  def func(self):
    # print(self.__sex)
    self.__sing()

zs=Person('张三',45,'男')
# print(zs.__dict__) #可以获取当前对象的所有属性
# print(zs.__dir__()) #可以获取当前对象的方法
# print(Person.__dict__) #可以获取当前对象的所有成员信息

# print(zs.name)
zs.func()