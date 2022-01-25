from os import scandir, system
import requests

url="https://www.pearvideo.com/video_1750164"

contId=url.split("_")[1]

# 获取视频流的接口地址
videoDataUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.05173156070661267"

res=requests.get(videoDataUrl,headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
  "Referer": url
})

srcUrl=res.json()['videoInfo']['videos']['srcUrl']
systemTime=res.json()['systemTime']

srcUrl=srcUrl.replace(systemTime,f'cont-{contId}')

with open("梨视频/a.mp4",mode="wb") as f:
   f.write(requests.get(srcUrl).content)





