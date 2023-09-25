while True:
    a, b = input().split()
    if int(a) == int(b) == 0:
        break
    else:
        b = b.replace(a, '')
        if b == '':
            b = 0
        print(int(b))
    