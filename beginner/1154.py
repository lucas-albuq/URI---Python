age = int(input())
media = 0
count = 0
while age >= 0:
    media += age
    count += 1
    age = int(input())
print(f'{media/count:.2f}')