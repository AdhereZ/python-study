import requests
import re

# 爬m3u8文件

# obj=re.compile(r"url: '(?P<murl>.*?)',",re.S)

# headers = {
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
# }

# url="https://91kanju.com/vod-play/54812-1-1.html"
# res=requests.get(url,headers=headers)
# murl=obj.search(res.text).group('murl')
# print(murl)

# res2=requests.get(murl,headers=headers)


# with open('哲仁王后.m3u8',mode="wb") as f:
#      f.write(res2.content)

# res2.close()
# print('over!')

t=1
with open('哲仁王后.m3u8',mode="r") as f:
  for line in f:
    line=line.strip() # 
    if line.startswith('#'):
      continue
    res3=requests.get(line)
    x = open(f"video/{t}.ts",mode='wb')
    x.write(res3.content)
    x.close()
    res3.close()
    t+=1