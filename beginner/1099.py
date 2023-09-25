N = int(input())
for z in range(N):
    lista = list(map(int, input().split()))
    lista.sort()
    x, y = lista
    somaImpar = 0
    for a in range(x + 1, y):
        if a % 2 != 0:
            somaImpar += a
    print(somaImpar)
