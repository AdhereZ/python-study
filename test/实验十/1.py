class ShortInputException(Exception):
  #  自定义异常类
  def __init__(self,length,atleast):
    Exception.__init__(self)
    self.length=length
    self.atleast=atleast
try:
  s=input('请输入-->')
  if len(s) < 3:
    raise ShortInputException(len(s),3)
except EOFError:
  print('您输入了一个结束标记EOF')
except ShortInputException as x:
  print('ShortInputException: 输入的长度是 %d,长度至少应是 %d' %(x.length,x.atleast))

else:
  print('没有异常发生.')