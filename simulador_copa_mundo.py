def processa_partida(dicionario, timeA, gA, timeB, gB):
    selecaoA = dicionario.get(timeA)
    selecaoB = dicionario.get(timeB)
    if gA > gB:
        selecaoA[2] = selecaoA[2] + 1
        selecaoA[4] = selecaoA[4] + gA - gB
    elif gA < gB:
        selecaoB[2] = selecaoB[2] + 1
        selecaoB[4] = selecaoB[4] + gB - gA
    else:
        selecaoA[3] = selecaoA[3] + 1
        selecaoB[3] = selecaoB[3] + 1


grupos = {}
grupos['A'] = ['Catar', 'Holanda', 'Equador', 'Senegal']
grupos['B'] = ['Inglaterra', 'Irã', 'Estados Unidos', 'País de Gales']

selecoes = {}

selecoes['Catar'] = ['Catar', 'A', 0, 0, 0]
selecoes['Holanda'] = ['Holanda', 'A', 0, 0, 0]
selecoes['Equador'] = ['Equador', 'A', 0, 0, 0]
selecoes['Senegal'] = ['Senegal', 'A', 0, 0, 0]

selecoes['Inglaterra'] = ['Inglaterra', 'B', 0, 0, 0]
selecoes['Irã'] = ['Irã', 'B', 0, 0, 0]
selecoes['Estados Unidos'] = ['Estados Unidos', 'B', 0, 0, 0]
selecoes['País de Gales'] = ['País de Gales', 'B', 0, 0, 0]


mandante = input("Time A: ")
golTimeA = int(input("Informe os gols A:"))
visitante = input("Time B: ")
golTimeB = int(input("Informe os gols B:"))
processa_partida(selecoes, mandante, golTimeA, visitante, golTimeB)
