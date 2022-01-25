
# https://dushu.baidu.com/pc/detail?gid=4315646974

# 获取所有章节的接口
url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'

# 文章内容接口
content_url='https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"44306063500","cid":"4306063500|10166918","need_bookinfo":1}'

import requests
import asyncio
import aiohttp
import aiofiles

async def aiodownload(cid,title):
  content_url='https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|'+cid+'","need_bookinfo":1}'

  async with aiohttp.ClientSession() as s:
     async with s.get(content_url) as res:
        dic=await res.json()
        async with aiofiles.open(f'novel/{title}.txt',mode='w',encoding='utf-8') as f:
          await f.write(dic['data']['novel']['content'])

async def getCatalog(url):
  res=requests.get(url)
  items=res.json()['data']['novel']['items']
  tasks=[]
  for i in items:
    title=i['title']
    cid=i['cid']
    tasks.append(aiodownload(cid,title))
  await asyncio.wait(tasks)

if __name__ == "__main__":
  loop=asyncio.get_event_loop()
  loop.run_until_complete(getCatalog(url))
    