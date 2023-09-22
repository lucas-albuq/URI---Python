n1, n2, n3, n4 = input().split()
media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1)/10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame}')
    media_final = (exame + media) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {media_final}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final}')
    