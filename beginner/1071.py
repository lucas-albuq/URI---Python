x = int(input())
y = int(input())
lista = [x, y]
lista.sort()
y, x = lista
somaImpar = 0
for z in range(y + 1, x):
    if z % 2 != 0:
        somaImpar += z
print(somaImpar)        

        
        