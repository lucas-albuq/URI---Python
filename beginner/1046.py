hInicial, hFinal = map(int, input().split())
if hInicial == hFinal:
    print('O JOGO DUROU 24 HORA(S)')
elif hInicial > hFinal:
    print(f'O JOGO DUROU {(24 - hInicial) + hFinal} HORA(S)')
else:
    print(f'O JOGO DUROU {hFinal - hInicial} HORA(S)')