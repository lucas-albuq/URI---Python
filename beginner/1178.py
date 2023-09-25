N = []
num = float(input())
for x in range(100):
    N.append(num)
    num /= 2
    print(f'N[{x}] = {N[x]:.4f}')