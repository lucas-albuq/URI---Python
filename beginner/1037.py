num = float(input())
if 75 < num <= 100:
    print('Intervalo (75,100]')
elif 50 < num <= 75:
    print('Intervalo (50,75]')
elif 25 < num <= 50:
    print('Intervalo (25,50]')
elif 0 <= num <= 25:
    print('Intervalo [0,25]')
else:
    print('Fora de intervalo')