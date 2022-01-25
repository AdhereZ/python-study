import sys,os,pickle
os.chdir(sys.path[0])

with open('pickle.dat','rb') as f:
  n=pickle.load(f)
  for i in range(n):
    x=pickle.load(f)
    print(x)