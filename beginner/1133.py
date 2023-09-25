x = int(input())
y = int(input())
lista = [x, y]
lista.sort()
x, y = lista
for z in range(x + 1, y):
    if z % 5 == 2 or z % 5 == 3:
        print(z)