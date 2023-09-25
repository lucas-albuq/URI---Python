lista = list(map(int, input().split()))
lista.sort(reverse=True)
a, b, c = lista
if a >= b + c:
    print('Invalido')
elif a == b == c:
    print('Valido-Equilatero')
    if a**2 == b**2 + c**2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')
elif a != b and a !=c and b != c:
    print('Valido-Escaleno')
    if a**2 == b**2 + c**2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Valido-Isoceles')
    if a**2 == b**2 + c**2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')