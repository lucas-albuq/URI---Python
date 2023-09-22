val = float(input())
val = int(val * 100)

print('NOTAS:')
print(f'{val // 10000} nota(s) de R$ 100.00')
val = val % 10000
print(f'{val // 5000} nota(s) de R$ 50.00')
val = val % 5000
print(f'{val // 2000} nota(s) de R$ 20.00')
val = val % 2000
print(f'{val // 1000} nota(s) de R$ 10.00')
val = val % 1000
print(f'{val // 500} nota(s) de R$ 5.00')
val = val % 500
print(f'{val // 200} nota(s) de R$ 2.00')
val = val % 200

print('MOEDAS:')
print(f'{val // 100} moeda(s) de R$ 1.00')
val = val % 100
print(f'{val // 50} moeda(s) de R$ 0.50')
val = val % 50
print(f'{val // 25} moeda(s) de R$ 0.25')
val = val % 25
print(f'{val // 10} moeda(s) de R$ 0.10')
val = val % 10
print(f'{val // 5} moeda(s) de R$ 0.05')
val = val % 5
print(f'{val} moeda(s) de R$ 0.01')