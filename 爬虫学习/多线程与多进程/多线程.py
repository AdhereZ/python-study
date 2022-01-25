from threading import Thread

# def func(name):
#     for i in range(1000):
#       print(f'{name}{i}')


# if __name__ == '__main__':
#   t1=Thread(target=func,args=('NO1',))  #args必须是元组，如果只穿一个参数后面要加逗号
#   t1.start()
#   t2=Thread(target=func,args=('NO2',))
#   t2.start()
#   for i in range(1000):
#     print(f'main{i}')

# class MyThread(Thread):
#   def run(self):
#     for i in range(1000):
#       print(f'子线程{i}')

# if __name__ == '__main__':
#   t=MyThread()
#   t.start()
#   for i in range(1000):
#     print(f"主线程{i}")