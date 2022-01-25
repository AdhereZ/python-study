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

async def main():
  #第一种方法
  # f=func()
  # await f

  # 第二种方法（推荐）
  tasks=[func(),func1(),func2()]
  await asyncio.wait(tasks)



if __name__ == "__main__":
   t1=time.time()
   asyncio.run(main())
   t2=time.time()
   print(t2-t1)