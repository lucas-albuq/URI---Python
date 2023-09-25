qtd = int(input())
count = 0
for z in range(qtd):
  x, y = map(int, input().split())
  soma = []
  count = 0
  while count < y:
      if x % 2 != 0:
         soma.append(x)
         count += 1
      x += 1
  print(sum(soma))
