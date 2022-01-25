import re
import requests
from lxml import etree

url="https://shenzhen.zbj.com/search/f/?kw=saas"
res=requests.get(url)

html=etree.HTML(res.text)

divs=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for d in divs:
  price=d.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0]
  title="saas".join(d.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
  com_name=d.xpath("./div/div/a[1]/div[1]/p/text()")[1][2:]
  address=d.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
  print(title,com_name,price,address)
