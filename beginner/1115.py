while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    elif x > 0 < y:
        print('primeiro')
    elif x < 0 < y:
        print('segundo')
    elif x < 0 > y:
        print('terceiro')
    elif x > 0 > y:
        print('quarto')