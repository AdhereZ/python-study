a=input('输入一个字符串：')
d=dict()
for ch in a:
  d[ch]=d.get(ch,0)+1
# m=max(d,key=d.get)
# print(m+':',d[m])
maxCommon=max(d.items(),key=lambda item: item[1])
print(maxCommon)