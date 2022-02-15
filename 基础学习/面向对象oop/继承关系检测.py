class A:
  pass

class B(A):
  pass

class C(A):
  pass

class D(B,C):
  pass

res = issubclass(D,B) #检测D类是不是B类的子类
res1 = issubclass(D,A) #检测D类是不是A类的子类
res2 = issubclass(A,D) #检测A类是不是sD类的子类
print(res2) 

