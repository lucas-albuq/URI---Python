positiveNumbers = 0
media = 0
for x in range (6):
    number = float(input())
    if number > 0:
        positiveNumbers += 1
        media += number
print(f'{positiveNumbers} valores positivos')
print(f'{media/positiveNumbers:.1f}')