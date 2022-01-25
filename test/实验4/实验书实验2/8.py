a=eval(input('输入只有两个整数的列表'))
b=eval(input('输入只有两个整数的列表'))

print(sum(map(lambda i,j:abs(i-j),a,b)))
