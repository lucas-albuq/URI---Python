while True:
    x = int(input())
    if x == 0:
      break
    else:
      for y in range(1, x):
        print(y, end=' ')
      print(x)