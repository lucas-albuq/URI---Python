x = int(input())
z = int(input())
qtd = 1
count = x
while z <= x:
    z = int(input())
while count <= z:
    x += 1
    count += x
    qtd += 1
print(qtd)
    