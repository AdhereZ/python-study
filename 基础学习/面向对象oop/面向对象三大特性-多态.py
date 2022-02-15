

class Computer():
   def usb(self,obj):
     obj.start()

class Mouse():
  def start(self):
    print('点击')

class keyboard():
  def start(self):
    print('键盘启动成功')

class Udisk():
  def start(self):
    print('U盘启动成功')

c=Computer()
m=Mouse()
k=keyboard()
u=Udisk()

c.usb(m)
c.usb(k)
c.usb(u)