import threading
from random import randint
from time import sleep


class Producer(threading.Thread):
  def __init__(self,threadname):
    threading.Thread.__init__(self,name=threadname)

  def run(self):
    global x
    while True:
      sleep(1)
      con.acquire()
      if len(x) == 5:
        print('Producer is waiting...')
        con.wait()
      else:
        r = randint(1,1000)
        x.append(r)
        print('Producer is:',r)
        con.notify()
      con.release()


class Consumer(threading.Thread):
    def __init__(self,threadname):
      threading.Thread.__init__(self,name=threadname)
    
    def run(self):
      global x
      while True:
        sleep(3)
        con.acquire()
        if not x:
          print('Consumer is waiting...')
          con.wait()
        else:
          print('Consumer is:',x.pop(0))
          con.notify()
        con.release()
      

con=threading.Condition()
x=[]
producer=Producer('producer')
consumer=Consumer('consumer')
producer.start()
consumer.start()

