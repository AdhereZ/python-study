import os, sys                                                                                   #1
os.chdir(sys.path[0])                                                                            #2
filename = 'demo.py'                                                                             #3
with open(filename,'r') as fp:                                                                   #4
   lines=fp.readlines()                                                                          #5
maxlen = len(max(lines,key=len))                                                                 #6
                                                                                                 #7
lines = [line.rstrip().ljust(maxlen)+'#'+str(index+1) + '\n' for index,line in enumerate(lines)] #8
print(lines)                                                                                     #9
with open(filename[:-3]+'_new.py','w') as fp:                                                    #10
  fp.writelines(lines)                                                                           #11
