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

timeA = selecoes[mandante]
timeB = selecoes.get(visitante)