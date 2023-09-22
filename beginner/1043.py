A, B, C = map(float, input().split())

if A >= B + C or B >= A + C or C >= B + A:
    print(f'Area = {((A + B) * C)/2}')
else:
    print(f'Perimetro = {A + B + C}')
    