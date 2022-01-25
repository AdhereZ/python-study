import asyncio
import aiohttp
import aiofiles

urls=[
  "http://kr.shanghai-jiuxin.com/file/bizhi/20211201/ku05vxfz4c3.jpg",
  "http://kr.shanghai-jiuxin.com/file/2020/0909/9a9e6e9bfdc888a7e46bb1ceaca479f2.jpg",
  "http://kr.shanghai-jiuxin.com/file/2021/0302/62d49686ba42a6655e880cd03e9123df.jpg"
  ]


async def aiodownload(url):
  # aiohttp.ClientSession() <===> requests
  # 用with是因为上下文管理器，也就是用完会自动关闭
  name=url.split('/')[-1]
  print(name)
  async with aiohttp.ClientSession() as s:
    async with s.get(url) as res:
      img=await res.content.read()
      async with aiofiles.open(f'img/{name}',mode='wb') as f:
        await f.write(img)
  
  print(name,'下载完成')

async def main():
  tasks=[]
  for u in urls:
    tasks.append(aiodownload(u))
  
  await asyncio.wait(tasks)

if __name__ == "__main__":
  loop=asyncio.get_event_loop()
  loop.run_until_complete(main())
  # asyncio.run(main()) #只写这一串会警告