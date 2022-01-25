from multiprocessing import Process

def func():
  for i in range(1000000):
    print(f'func{i}')


if __name__ == '__main__':
  p=Process(target=func)
  p.start()
  for i in range(10000000):
    print(f'main{i}')