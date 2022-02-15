class human():
  num=111
  def eat(self):
    print('吃饭')


class F(human):
  num=222
  def eat(self):
    super().eat()
    print(super().num)
    print('f吃饭')

class M(human):
  num=333
  def eat(self):
    super().eat()
    print(super().num)
    print('m喝水')

class s(F,M):
   num=444
   def eat(self):
      super().eat()
      print(super().num)
      print('s吃饭')

ss=s()
ss.eat()

# 继承的关系 s->F->M->human

# mro() 获取MRO列表 就是类的继承关系
print(s.mro())
# [<class '__main__.s'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.human'>, <class 'object'>]

