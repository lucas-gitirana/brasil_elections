vetores = []
secoes = []

cod = input('Código do município: ')

with open("eleicoes.csv", "r", encoding="utf8") as arquivo:
    linhas_arquivo = arquivo.readlines()
    for linha in linhas_arquivo:
        vetores.append(linha.split(";"))

    for vetor in vetores:
        if cod in vetor[11]:
            if vetor[14] not in secoes:
                secoes.append(vetor[11].replace('"', ''))
    
with open("secoes.txt", "w") as arq_secoes:
    for secao in secoes:
        aptos = 0
        comparecimentos = 0
        abstencoes = 0

        for vetor in vetores:
            if cod in vetor[11]:
                if secao in vetor[14]:
                    aptos += int(vetor[22].replace('"', ''))
                    comparecimentos += int(vetor[23].replace('"', ''))
                    abstencoes += int(vetor[24].replace('"', ''))
            arq_secoes.write(f'Secao: {secao} \nAptos: {aptos} \nComparecimentos: {comparecimentos} \nAbstencoes: {abstencoes}')        
            
