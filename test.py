result = 10

def test():
  global result
  result = 20
  print(result)

test()
print(result)