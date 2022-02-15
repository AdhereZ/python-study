import time
class mylog():
  filename=str(time.strftime('%Y-%m-%d'))+'.log'
  fileobj=None

  def __init__(self):
      self.fileobj=open(self.filename,mode='w',encoding='utf-8')

  def writelog(self,s):
    date=str(time.strftime('%Y-%m-%d %H:%M:%S'))+'\n'
    msg=date+s
    self.fileobj.write(msg)

  def __del__(self):
    self.fileobj.close()

l=mylog()
l.writelog('今天开始继续学习python的面向对象')