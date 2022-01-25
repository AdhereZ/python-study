b=[1,2,4,1,3,9,7,10,30,70,1]

def square(x):
   return x**2

#把map生成的迭代器转换成数组
a=list(map(square,b))

print('map\n',a,'\n')

print('any\n',any(('',0,False)),'\n')

print('all\n',all([]),'\n')

print('zip\n',list(zip([1,2,3],[4,5,6])),'\n')

