pergunta = 1
while pergunta == 1:
    media = 0
    notasvalidas = 0
    while notasvalidas != 2:
        nota = float(input())
        if 0 <= nota <= 10:
            media += nota
            notasvalidas += 1
        else:
            print('nota invalida')
    print(f'media = {media/2:.2f}')
    print('novo calculo (1-sim 2-nao)')
    pergunta = int(input())
    while pergunta < 1 or pergunta > 2:
        print('novo calculo (1-sim 2-nao)')
        pergunta = int(input())