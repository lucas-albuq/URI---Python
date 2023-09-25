while True:
    x = int(input())
    if x == 0:
      break
    if x % 2 != 0:
      x+=1
    soma = x
    for _ in range(4):
        x+=2
        soma+=x
    print(soma)