cod, qtd = map(float, input().split())
if cod == 1:
    cod = 4.0
elif cod == 2:
    cod = 4.5
elif cod == 3:
    cod = 5.0
elif cod == 4:
    cod = 2.0
elif cod == 5:
    cod = 1.5
    
print(f'Total: R$ {cod*qtd:.2f}')