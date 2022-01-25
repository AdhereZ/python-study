import requests
import re
import csv

url='https://www.dydytt.net/index2.htm'
domain="https://www.dydytt.net"
res=requests.get(url)
res.encoding='gb2312' #设置编码方式，默认是utf-8
res.close()
obj=re.compile(r'2021新片精品.*?<table width="100%" border="0" cellspacing="0" cellpadding="0">(?P<table>.*?)</table>',re.S)
obj2=re.compile(r"<a href='(?P<h>.*?)'.*?</a><br/>",re.S)
it=obj.finditer(res.text)
childList=[]
for i in it:
  x=i.group('table')
  res=obj2.finditer(x)
  for j in res:
    ch=domain+j.group('h')
    childList.append(ch)

# 弹出第一个网址
childList.pop(0)
obj3=re.compile(r'◎译　　名(?P<name>.*?)<br />.*?<br /><a target="_blank" href="(?P<mh>.*?)">.*?<center>',re.S)

f = open('电影天堂2021新片精品.csv',mode="w",encoding='utf-8',newline='') #newline=''是为了解决生成文件每隔一条数据都会空一行
csvwriter = csv.writer(f)


for href in childList:
  cr=requests.get(href)
  cr.encoding='gb2312'
  res3=obj3.search(cr.text)
  print(res3.group('name'))
  dic=res3.groupdict()
  dic['name']=dic['name'].strip()
  csvwriter.writerow(dic.values())

f.close()
cr.close()
print('over')