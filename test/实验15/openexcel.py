from random import choice,randrange
from string import digits,ascii_letters
from os import listdir,mkdir
import os,sys
from os.path import isdir
from openpyxl import Workbook,load_workbook

# 使能够使用相对路径
os.chdir(sys.path[0])

def createExcel():
    if not isdir('xlsxs'):
      mkdir('xlsxs')
    
    global total
    characters=digits+ascii_letters
    
    for i in range(50):
      xlsName = 'xlsxs\\{i}.xlsx'
      totalLines = randrange(10**4)
      
   