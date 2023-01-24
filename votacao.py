# ITEM A
with open("eleicoes.csv", "r", encoding="utf-8") as arq_eleicoes:
    linhas = arq_eleicoes.readlines()
    cds_municipio = []
    nms_municipio = []
    for linha in linhas:
        array_linha = linha.split(';')
        if array_linha[11] not in cds_municipio:
            cds_municipio.append(array_linha[11])
            nms_municipio.append(array_linha[12])

    with open("lista_municipios.txt", "w") as arq_municipios:
        for i in range(len(cds_municipio)):   
            arq_municipios.write(f'{cds_municipio[i]} - {nms_municipio[i]} \n')
            