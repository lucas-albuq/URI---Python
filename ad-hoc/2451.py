def max_comida(tabuleiro, N):
  max_comida = 0
  comida = 0
  direcao = 1
  j = 0
  for _ in range(N):
    j = 0 if direcao == 1 else N-1
    while 0 <= j < N:
      if tabuleiro[_][j] == 'o':
        comida +=1
      elif tabuleiro[_][j] == 'A':
        max_comida = max(max_comida, comida)
        comida = 0
      j+= direcao
    direcao *= -1
  return max(max_comida, comida)  

N = int(input())
tabuleiro = []
for _ in range(N):
  linha = list(input())
  tabuleiro.append(linha)
print(max_comida(tabuleiro, N))