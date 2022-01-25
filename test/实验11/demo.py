import re
import tkinter as tk
import tkinter.messagebox
root = tk.Tk()
root.geometry('400x280+400+200')
root.resizable(False,False) # 不能改变窗口大小
root.title('简易计算器')

# 设置文本框，只读
contentVar = tk.StringVar(root, '')
contentEntry = tk.Entry(root, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10, y=10, width=360, height=40)

def buttonClick(btn):
    content = contentVar.get()
    # 判断当前是否有小数点，有就加0
    if content.startswith('.'):
        content = '0.' + btn
    # 不同按钮的功能定义
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        # 超过一个小数点报错
        lastpart = re.split(r'\+|-|\*|/',content)[-1] # 将整个表达式按照运算符进行分割，且取最后一个分割组
        if '.' in lastpart:
            tkinter.messagebox.showerror('错误', '小数点太多')
            return
        else:
            content += btn
    elif btn == 'C' :
        content = ''
    elif btn == '=':    # 计算
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    elif btn in operators:
        # 仅能一个连续符号，不能连续多个运算符
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误', '不能连续两个符号')
            return
        content += btn
    contentVar.set(content)

operators = ('+', '-', '*', '/')
# 放置各按键 按钮高40，竖直间隔15，长100.水平间隔20
digits = list('.+-123456789')
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tk.Button(root, text=d, command= lambda x=d:buttonClick(x))
        btnDigit.place(x=20+col*100, y=70+row*45, width=65, height=28)
conponent = ('*', '/', '=', 'C')
for index, s in enumerate(conponent):
    btnOpt = tk.Button(root, text=s, command=lambda x=s:buttonClick(x))
    btnOpt.place(x=320, y=70+index*45, width=65, height=28)
    
root.mainloop() 
