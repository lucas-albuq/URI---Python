grenal = 1
iV = 0
gV = 0
emp = 0
count = 0
while grenal == 1:
    i, g = map(int, input().split())
    if i > g:
        iV += 1
    elif g > 1:
        gV += 1
    else:
        emp += 1
    print('Novo grenal (1-sim 2-nao)')
    grenal = int(input())
    count +=1
print(f'{count} grenais')
print(f'Inter:{iV}')
print(f'Gremio:{gV}')
print(f'Empates:{emp}')
if iV > gV:
    print('Inter venceu mais')
elif gV > iV:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
        