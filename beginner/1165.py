n = int(input())
for x in range(n):
    num = int(input())
    primo = 's'
    for x in range(2, num):
        if num % x == 0:
            primo = 'n'
    if primo == 's':
      print(f'{num} eh primo')
    if primo == 'n':
      print(f'{num} nao eh primo')