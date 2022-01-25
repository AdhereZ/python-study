import sys,os,pickle
os.chdir(sys.path[0])
data = ['a','b','c','d']

with open('pickle.dat','wb') as f: 
  try:
    pickle.dump(len(data),f)
    for item in data:
      pickle.dump(item,f)
  except:
    print('写文件异常！')
    