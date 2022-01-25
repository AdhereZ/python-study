def multiple(x):
    sum = 1 
    for i in x:
      sum*=i
    return sum 

a=input('输入一个列表\n').split(',')
a1=[int(a[i]) for i in range(len(a))]
print(multiple(a1))