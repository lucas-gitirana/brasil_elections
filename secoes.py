secoes = []
vetores = []

codigo = input('Código do município: ')

with open("eleicoes.csv", "r", encoding="utf8") as arquivo:    
    linhas = arquivo.readlines()

    for linha in linhas:
        vetor = linha.split(';')
        if codigo in vetor[11]:
            nome = vetor[12]
            vetores.append(linha.split(';'))

    with open("secoes.txt", "w") as arq_secoes:
        arq_secoes.write(f'{nome}\n')
        arq_secoes.write(f'--------------------------\n\n')
        for vetor in vetores:        
            if vetor[14] not in secoes:
                secoes.append(vetor[14])                    
                arq_secoes.write(f'Secao: {vetor[14]}\nAptos: {vetor[22]} \nComparecimentos: {vetor[23]} \nAbstencoes: {vetor[24]}\n\n')        
            
