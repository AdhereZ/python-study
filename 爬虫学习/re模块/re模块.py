import re

# # findall: 匹配字符串中所有的符合正则的内容（不常用，返回的是列表效率低）
# l=re.findall(r"\d+","我的电话是：10086，警察的电话是：110")
# print(l)

# # finditer: 匹配字符串的中所有的内容（返回迭代器）从迭代器中拿到内容需要.group()
# it= re.finditer(r"\d+","我的电话是：10086，警察的电话是：110")
# for i in it:
#   print(i.group())

# # search：找到一个结果就返回
# s=re.search(r"\d+","我的电话是：10086，警察的电话是：110")
# print(s.group())


# # match是从头开始匹配
# m=re.match(r"\d+","10086，警察的电话是：110")
# print(m)


# 预加载正则表达式
obj=re.compile(r'\d+')

res = obj.finditer("我的电话是：10086，警察的电话是：110")
for i in res:
  print(i.group())