nameSeller = input().upper()
sellerSalary = float(input())
sellerSales = float(input())

comission = (15/100) * sellerSales

print(f'TOTAL = R$ {sellerSalary + comission:.2f}')
