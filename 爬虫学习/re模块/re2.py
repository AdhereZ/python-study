import re

s="""
<div class="jj"><span id="1">林俊杰</span></div>
<div class="jay"><span id="2">周杰伦</span></div>
<div class="gd"><span id="3">权志龙</span></div>
<div class="gai"><span id="4">gai</span></div>
"""
# (?P<分组名字>正则) 可以单独从正则匹配的内容中提取到自己想要的内容
obj=re.compile(r'<div class="(?P<class>.*?)"><span id="(?P<id>.*?)">(?P<name>.*?)</span></div>',re.S) #re.S让.能匹配换行符
result=obj.finditer(s)

for it in result:
  print(it.group('class'),it.group('id'),it.group('name'))