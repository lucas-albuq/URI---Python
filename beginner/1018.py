val = int(input())

val_100 = val // 100
val_50 = (val % 100) // 50
val_20 = ((val % 100) % 50) // 20
val_10 = (((val % 100) % 50) % 20) // 10
val_05 = ((((val % 100) % 50) % 20) % 10) // 5
val_02 = (((((val % 100) % 50) % 20) % 10) % 5) // 2
val_01 = (((((val % 100) % 50) % 20) % 10) % 5) % 2

print(val)
print(f'{val_100} nota(s) de R$ 100,00')
print(f'{val_50} nota(s) de R$ 50,00')
print(f'{val_20} nota(s) de R$ 20,00')
print(f'{val_10} nota(s) de R$ 10,00')
print(f'{val_05} nota(s) de R$ 5,00')
print(f'{val_02} nota(s) de R$ 2,00')
print(f'{val_01} nota(s) de R$ 1,00')