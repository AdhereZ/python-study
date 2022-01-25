import requests

url="https://fanyi.baidu.com/sug"
s = input('请输入你要翻译的英文单词')

data={
  "kw": s
}


res=requests.post(url,data=data)
print(res.json())
res.close()