par = []
impar = []
posPar = 0
posImpar = 0
for x in range(15):
    n = int(input())
    if len(par) == 5:
        for y in range(5):
            print(f'par[{y}] = {par[y]}')
        par = []
    if len(impar) == 5:
        for a in range(5):
            print(f'impar[{a}] = {impar[a]}')
        impar = []
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
for z in range(len(impar)):
    print(f'impar[{z}] = {impar[z]}')       
for i in range(len(par)):
    print(f'par[{i}] = {par[i]}')       
    