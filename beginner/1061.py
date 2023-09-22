n, d = input().split()
h, m, s = map(int, input().split(':'))
n, d2 = input().split()
h2, m2, s2 = map(int, input().split(':'))

qtdD = int(d2) - int(d)
qtdH = h2 - h
qtdM = m2 - m
qtdS = s2 - s

if qtdH < 0:
  qtdH += 24
  qtdD -= 1
if qtdH == 0:
  if qtdM < 0 and qtdS >= 0:
    qtdM += 60
    qtdH += 23
    qtdD -= 1
  elif qtdS < 0 and qtdM >= 0:
    qtdS += 60
    qtdM -= 1
    qtdH += 23
    qtdD -= 1
  elif qtdM < 0 and qtdS < 0:
    qtdS += 60
    qtdM += 59
    qtdH += 23
    qtdD -= 1
else:
  if qtdM < 0:
    qtdM += 60
    qtdH -= 1
  if qtdS < 0:
    qtdS += 60
    qtdM -=1

print(f'{qtdD} dia(s)')
print(f'{qtdH} hora(s)')
print(f'{qtdM} minuto(s)')
print(f'{qtdS} segundo(s)')
