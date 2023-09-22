N = int(input())
dentro = 0
fora = 0
for x in range(N):
    num = int(input())
    if 10<= num <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')