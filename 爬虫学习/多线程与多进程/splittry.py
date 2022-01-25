urls=[
  "http://kr.shanghai-jiuxin.com/file/bizhi/20211201/ku05vxfz4c3.jpg",
  "http://kr.shanghai-jiuxin.com/file/2020/0909/9a9e6e9bfdc888a7e46bb1ceaca479f2.jpg",
  "http://kr.shanghai-jiuxin.com/file/2021/0302/62d49686ba42a6655e880cd03e9123df.jpg"
  ]

for u in urls:
  name=u.split('/')[-1]
  print(name)