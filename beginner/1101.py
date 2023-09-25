soma = 0
while True:
    lista = list(map(int, input().split()))
    lista.sort()
    M, N = lista
    if M <= 0:
        break
    else:
        soma = 0
        for x in range(M, N + 1):
            print(x, end=' ')
            soma += x
        print(f'Sum={soma}')
