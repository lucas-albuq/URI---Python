hI, mI, hF, mF = map(int, input().split())
if hI == mI == hF == mF:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hI == hF and mI > mF:
    print(f'O JOGO DUROU 23 HORA(S) E {(60 - mI) + mF} MINUTO(S)')
elif hI == hF and mI < mF:
    print(f'O JOGO DUROU 0 HORA(S) E {mF - mI} MINUTO(S)')
elif hI < hF and mI < mF:
    print(f'O JOGO DUROU {hF - hI} HORA(S) E {mF - mI} MINUTO(S)')
elif hF == hI + 1 and mI > mF:
    print(f'O JOGO DUROU 0 HORA(S) E {(60 - mI) + mF} MINUTO(S)')
elif hI > hF and mI > mF:
    print(f'O JOGO DUROU {((24 - hI) + hF) - 1} HORA(S) E {(60 - mI) + mF} MINUTO(S)')
elif hI > hF and mI < mF:
  print(f'O JOGO DUROU {(24 - hI) + hF} HORA(S) E {mF - mI} MINUTO(S)')
elif hI < hF and mI > mF:
  print(f'O JOGO DUROU {(hF - hI) -1} HORA(S) E {(60 - mI) + mF} MINUTO(S)')
elif hI > hF:
  print(f'O JOGO DUROU {(24 - hI) + hF} HORA(S) E 0 MINUTO(S)')
else:
  print(f'O JOGO DUROU {hF - hI} HORA(S) E 0 MINUTO(S)')
  