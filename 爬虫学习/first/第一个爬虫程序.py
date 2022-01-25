from urllib.request import urlopen


url= "https://juejin.cn/"
res = urlopen(url)


with open('爬虫.html',mode="w",encoding='utf-8') as f:
  f.write(res.read().decode('utf-8'))

print('over')
res.close()