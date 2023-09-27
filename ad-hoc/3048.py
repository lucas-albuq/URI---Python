N = int(input())
seq = 0
ultimo = 0

for _ in range(N):
  v = int(input())
  if v != ultimo:
    seq+=1
  ultimo = v
print(seq)