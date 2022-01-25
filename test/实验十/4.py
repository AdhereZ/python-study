for i in range(-2,5):
  try:
    assert i>0
    print(i)
  except:
    print('i小于0')