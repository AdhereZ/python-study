from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
  for i in range(1000):
    print(name,i)


if __name__ == "__main__":
   with ThreadPoolExecutor(100) as t:
     for i in range(100):
       t.submit(fn,name=f'线程{i}')
   print('123')