import json
data = json.load(open('D:/pythonProject/test/实验九/db.json'))

for key,value in data.items():
  print(key,':',value)
  print()