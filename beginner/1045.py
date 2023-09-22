num = list(map(float, input().split()))
num.sort(reverse = True)
A, B, C = num
if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B != C or A == C != B or B == C != A:
        print('TRIANGULO ISOSCELES')
