import csv
import requests
import re

pagenum=input('请输入你想要的页数')
pagenum=(int(pagenum)-1)*25
url=f"https://movie.douban.com/top250?start={pagenum}"
headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

res=requests.get(url,headers=headers)
pc=res.text

obj=re.compile(r'<li>.*? <span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
ret=obj.finditer(pc)
f = open('data.csv',mode="w",encoding='utf-8',newline='') #newline=''是为了解决生成文件每隔一条数据都会空一行
csvwriter = csv.writer(f)

for i in ret:
  # strip()是因为年份前面有很大的空格，用这个消除空格
  # print(i.group('name'),i.group('year').strip(),i.group('score'),i.group('num'))
  dic=i.groupdict() #将迭代器转换成字典
  dic['year'] = dic['year'].strip()
  csvwriter.writerow(dic.values()) #写一行数据

f.close()
res.close()

print('over!') 
