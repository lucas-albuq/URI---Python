valor = float(input())
taxa = 0
if valor <= 2000:
    print('Isento')
elif valor <= 3000:
    taxa = (valor - 2000) * 8/100
    print(f'R$ {taxa:.2f}')
elif valor <= 4500:
    taxa = (valor - 3000) * 18/100 + 1000 * 8/100
    print(f'R$ {taxa:.2f}')
else:
    taxa = (valor - 4500) * 28/100 + 1500 * 18/100 + 1000 * 8/100
    print(f'R$ {taxa:.2f}')
    