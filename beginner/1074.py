N = int(input())
for x in range(N):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    elif num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num > 0:
        print('ODD POSITIVE')
    else:
        print('ODD NEGATIVE')