def testEscada(matriz, N, M):
  k = 0
  while k != N:
    if sum(matriz[k]) == 0:
      while k < N-1:
        k +=1
        if sum(matriz[k]) != 0:
          return 'N'
      break
    for i in range(M):
      if matriz[k][i] != 0:
        kk = k
        ii = i
        while ii > 0:
          ii -= 1
          if matriz[k][ii] != 0:
            return 'N'
        while kk < N-1:
          kk += 1
          if matriz[kk][i] != 0:
            return 'N'
        k+=1
        if k == N:
          break
  return 'S'

N, M = map(int, input().split())
matriz = []
for k in range(N):
  linha = list(map(int, input().split()))
  matriz.append(linha)
print(testEscada(matriz, N, M))
