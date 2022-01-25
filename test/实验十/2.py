import sys,os
os.chdir(sys.path[0])

try:
  with open('1.txt','r') as fp:
    lines=fp.readlines()
except:
  with open('1.txt','w') as fp:
    strs=['2222\n','213465\n']
    fp.writelines(strs)