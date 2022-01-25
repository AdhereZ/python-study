import os, sys
os.chdir(sys.path[0])
filename = 'demo.py'
with open(filename,'r') as fp: 
   lines=fp.readlines()
maxlen = len(max(lines,key=len))

lines = [line.rstrip().ljust(maxlen)+'#'+str(index+1) + '\n' for index,line in enumerate(lines)]
print(lines)
with open(filename[:-3]+'_new.py','w') as fp:
  fp.writelines(lines)
