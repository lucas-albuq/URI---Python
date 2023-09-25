I = 1
J = 7
maiorJ = 5
while I <=9:
    maiorJ += 2
    J = maiorJ
    for x in range(3):
        print(f'I={I} J={J}')
        J -=1
    I += 2