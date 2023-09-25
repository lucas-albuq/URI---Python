fib = [0, 1]
n = int(input())
for x in range(n):
    a = int(input())
    if a > 1:
        for y in range(len(fib), a + 1):
            f = fib[y - 1] + fib[y - 2]
            fib.append(f)
    print(f'Fib({a}) = {fib[a]}')