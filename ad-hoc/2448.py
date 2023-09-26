N, M = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

p = {x[i]: i for i in range(N)}

t = 0
ultimo = 0

for _ in y:
  indice = p[_]
  t += abs(ultimo - indice)
  ultimo = indice

print(t)
