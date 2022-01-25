from hashlib import new
import requests
import csv
from concurrent.futures import ThreadPoolExecutor

data={
"limit": 20,
"current": 1,
"pubDateStartTime": "",
"pubDateEndTime": "",
"prodPcatid": "",
"prodCatid": "",
"prodName": ""
}

url="http://www.xinfadi.com.cn/getPriceData.html"

f=open('data.csv',mode='w',encoding='utf-8',newline='')
csvwriter=csv.writer(f)

def download_one_page(url,data,index):
  print(index)
  data["current"]=index
  res=requests.post(url,data=data)
  lis=res.json()['list']
  for l in lis:
    csvwriter.writerow(l.values())
  print(f'page{index} over!')
  res.close()



if __name__ == "__main__":
   with ThreadPoolExecutor(20) as t:
      for i in range(1,200):
        t.submit(download_one_page,url=url,data=data,index=i)
 
      
   print('all over')  
