alcool = 0
gasolina = 0
diesel = 0
while True:
    num = int(input())
    if 0 < num < 4:
        if num == 1:
            alcool += 1
        elif num == 2:
            gasolina += 1
        else:
            diesel += 1
    elif num == 4:
        break
print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
        