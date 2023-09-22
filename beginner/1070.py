num = int(input())
qtdPrints = 0
while qtdPrints != 6:
    if num % 2 != 0:
        print(num)
        qtdPrints += 1
        num +=1
    else:
        num +=1