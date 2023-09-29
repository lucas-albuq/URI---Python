def determinar_signo(data):
    datas_inicio_signos = [
        (3, 21), (4, 21), (5, 21), (6, 21), (7, 23), (8, 23),
        (9, 23), (10, 23), (11, 22), (12, 22), (1, 20), (2, 19)
    ]
    
    dia, mes = map(int, data.split('/'))
    
    for i in range(len(datas_inicio_signos)):
        mes_inicio, dia_inicio = datas_inicio_signos[i]
        mes_fim, dia_fim = datas_inicio_signos[(i + 1) % len(datas_inicio_signos)]
        
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fim and dia <= dia_fim):
            return ["aries", "touro", "gemeos", "cancer", "leao", "virgem", "libra", "escorpiao", "sagitario", "capricornio", "aquario", "peixes"][i]


data_nascimento = input()

signo = determinar_signo(data_nascimento)
print(signo)
