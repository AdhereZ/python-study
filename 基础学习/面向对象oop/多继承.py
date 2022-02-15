class F():
  def eat(self):
    print('吃饭')

class M():
  def drink(self):
    print('喝水')

class s(F,M):
   pass

ss=s()
ss.eat()
ss.drink()