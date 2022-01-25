print('my name is {name},age is {age}'.format(name='zjh',age=20))
position = (5,8,13)
print('x: {0[0]}, y: {0[1]}, z: {0[2]}'.format(position))
weather = [('Tom','bad'),('jack','lucky'),('bob','happy'),('james','strong')]
formatter = '{0[0]} is {0[1]}'.format
for item in map(formatter,weather):
    print(item)