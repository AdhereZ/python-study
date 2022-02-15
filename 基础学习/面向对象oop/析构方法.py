# __del__析构方法
#   当前实例化对象被销毁时，自动触发
    # 作用：可以完成一些特殊任务，如，初始化方法打开的文件，可以在析构方法中关掉

# 1

import time

class writeLog():
  filename=str(time.strftime('%Y-%m-%d'))+'.txt'

  def __init__(self):
    self.file=open(self.filename,mode='w',encoding='utf-8')

  def log(self,s):
     self.file.write(s)
  
  def __del__(self):
    self.file.close()
    print('over')



w=writeLog()
w.log('本节内容学了类的析构方法，写点代码测试一下')



# 2

# class Cart(): 
#   brand=''
  
#   def __init__(self,brand):
#     self.brand=brand
#     print(f'{self.brand}汽车创建')
  
#   def __del__(self):
#     print(f'{self.brand}汽车销毁')

# Cart('宝马')
# Cart('奔驰')
# Cart('法拉利')

# 输出结果
# 宝马汽车创建
# 宝马汽车销毁
# 奔驰汽车创建
# 奔驰汽车销毁
# 法拉利汽车创建
# 法拉利汽车销毁