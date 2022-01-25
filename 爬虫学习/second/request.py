import requests

name=input('输入一个明星的名字')
url=f"https://www.baidu.com/s?wd={name}&rsv_spt=1&rsv_iqid=0xba6507e70000af21&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=10&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6&rsp=5&inputT=3165&rsv_sug4=3165"

headers= {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
res=requests.get(url,headers=headers)
print(res.text)

with open('mybaidu.html',mode="w",encoding="utf-8") as f:
  f.write(res.text)

res.close()