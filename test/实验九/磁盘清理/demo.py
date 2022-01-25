import sys
from os.path import isdir,splitext,join,getsize
from os import listdir,remove

fileTypes = ['.tmp','.log','.obj','.txt'] 

def delFile(directory):
    if not isdir(directory):
      return
    for filename in listdir(directory):
        f=join(directory,filename)
        if isdir(f):
          delFile(f)
        elif splitext(f)[1] in fileTypes or getsize(f) == 0:
          remove(f)
          print(f,'detele...')

d=sys.argv[1]
delFile(d)