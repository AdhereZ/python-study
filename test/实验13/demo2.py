from multiprocessing import Pool
import time

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




if __name__ == '__main__':
  print('多进程')
  t1 = int(time.time())
  with Pool(2) as p:
    print(sum(p.map(isPrime,range(1000000))))
  t2 = int(time.time())
  print('所用时间(s): ', t2-t1)





