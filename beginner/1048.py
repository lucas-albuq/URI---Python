salario = float(input())
reajuste = 0
porcentagem = 0
if salario <= 400:
    reajuste = salario * 15/100
    salario += reajuste
    porcentagem = 15
elif salario <= 800:
    reajuste = salario * 12/100
    salario += reajuste
    porcentagem = 12
elif salario <= 1200:
    reajuste = salario * 10/100
    salario += reajuste
    porcentagem = 10
elif salario <= 2000:
    reajuste = salario * 7/100
    salario += reajuste
    porcentagem = 7
else:
    reajuste = salario * 4/100
    salario += reajuste
    porcentagem = 4
    
print(f'Novo salario: {salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem} %')
    