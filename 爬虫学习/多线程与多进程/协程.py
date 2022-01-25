# 协程： 当程序遇见了IO操作时，可以选择性的切换到其他任务身上

import asyncio
import time

async def func():
  print('hello world')
  # time.sleep(3) #当程序出现同步操作的时候，异步就中断了
  await asyncio.sleep(3) #异步操作的代码
  print('func')

async def func1():
  print('hello world1')
  # time.sleep(2)
  await asyncio.sleep(2)
  print('func1')

async def func2():
  print('hello world2')
  # time.sleep(4)
  await asyncio.sleep(4)
  print('func2')


if __name__ == "__main__":
   g=func()
   g1=func1()
   g2=func2()
   tasks=[g,g1,g2]
   t1=time.time()
   asyncio.run(asyncio.wait(tasks)) #多个任务一起跑要用wait
   t2=time.time()
   print(t2-t1)