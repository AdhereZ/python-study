from multiprocessing import Pool

def isPrime(n):
  if n<2:
    return 0
 
  if n==2:
    return 1
  
  if not n&1:  #判定奇偶 偶数返回0
    return 0
  
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return 0
  
  return 1

p=int(input('请输入一个整数 '))

if isPrime(p):
   print(str(p)+'是素数')
else: 
   print(str(p)+'不是素数')

