valores = list(map(int, input().split()))
a = valores[0]
ultimo_valor = len(valores) - 1
n = valores[ultimo_valor]
resultado = 0
for x in range(n):
    resultado += a + x
print(resultado)
