import requests
from bs4 import BeautifulSoup
import time

url="https://umei.cc/"
res=requests.get(url)
res.encoding='utf-8'
s=res.text
res.close()
mp=BeautifulSoup(s,'html.parser')
lis=mp.find("div",class_="PicListTxt").find_all('li')
slist=[]
for i in lis:
  href=i.find("a").get('href')
  chref=url+href
  res1=requests.get(chref)
  res1.encoding='utf-8'
  imgb=BeautifulSoup(res1.text,'html.parser')
  img=imgb.find("div",class_="ImageBody").find("img")
  src=img.get("src")
  slist.append(src)
  # 下载图片
  img_resp=requests.get(src)
  image_name=src.split("/")[-1] #以/为分割形成列表，取最后一个元素
  with open(f"img/{image_name}",mode="wb")  as f:
     f.write(img_resp.content) #写入图片内容,这个内容是二进制的字节
  print("over",image_name)
  time.sleep(1)
  res1.close()

print("all over")



