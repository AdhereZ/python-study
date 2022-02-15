""" 
定义一个接口规范类，其他类都继承这个类，并实现（重写）父类中的方法
由于每个对象实现父类方法的方式或者过程都不相同，最后的结果是不一样的形态
"""

class USB():
  def start():
    pass

class Mouse(USB):
  def start(self):
    print('点击')

class keyboard(USB):
  def start(self):
    print('键盘启动成功')

class Udisk(USB):
  def start(self):
    print('U盘启动成功')

m=Mouse()
m.start()