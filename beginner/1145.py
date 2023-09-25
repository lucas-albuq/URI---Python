x, y = map(int, input().split())
for z in range(1, y + 1, x):
  for a in range(x - 1):
    print(f'{z}', end = ' ')
    z+=1
  print(z)