from decimal import Decimal
I = 0
J = 0
while I <= 2:
  J = 1 + I
  if float(J) % 1 == 0:
    I = int(I)
    J = int(J)
  for x in range(3):
      print(f'I={I} J={J}')
      J +=1
  I += Decimal('0.2')