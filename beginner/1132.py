x = int(input())
y = int(input())
lista = [x, y]
lista.sort()
x, y = lista
soma = 0
for z in range(x, y + 1):
    if z % 13 != 0:
        soma += z
print(soma)