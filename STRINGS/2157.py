n = int(input())
for x in range(n):
    number = ''
    a, b = input().split()
    for x in range(int(a), int(b) + 1):
        number += str(x)
    number += ''.join(reversed(number))
    print(number)