from collections import deque


NC = int(input())

def survive(n, k):
  de = deque(n)
  for x in range(len(n)-1):
    de.rotate(-k)
    de.pop()
  return de[0]

for _ in range(NC):
  n, k = map(int, input().split())
  n = [x for x in range(1, n+1)]
  print(f"Case {_+1}: {survive(n, k)}")


