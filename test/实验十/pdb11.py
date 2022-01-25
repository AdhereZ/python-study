import pdb

class myDemo:
  def first(self):
    pdb.set_trace()
    for i in range(5):
      print(i)
  def second(self,b):
    pdb.set_trace()
    for i in b:
      print(i) 

x=myDemo()
x.first()
b=['a','b','c','d']
x.second(b)