secoes = []
vetores = []

codigo = input('Código do município: ')

with open("eleicoes.csv", "r", encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        vetor = linha.split(';')
        if codigo in vetor[11]:
            vetores.append(linha.split(';'))

    with open("eleicoes-municipios.txt", "w") as arq_secoes:
        soma_aptos = 0
        soma_comparecimentos = 0
        soma_abstencoes = 0

        for vetor in vetores:        
            if vetor[14] not in secoes:
                secoes.append(vetor[14])
                soma_aptos += int(vetor[22].replace('"', ''))
                soma_comparecimentos += int(vetor[23].replace('"', ''))
                soma_abstencoes += int(vetor[24].replace('"', ''))                   
            
            
        arq_secoes.write(f'Aptos: {soma_aptos}\nComparecimentos: {soma_comparecimentos}\nAbstencoes: {soma_abstencoes}\n')        
            
