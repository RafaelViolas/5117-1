# vendas de combustivel
# 1 Total
# 2 Total por estação
# 3 Total por Grupo
# 4 Qual a estação que tem mais vendas
# 5 Qual o grupo que vendeu menos
# 4a. Pode haver mais que uma, o mesmo com os grupos
def fmaiores(lista):
    festacoes = ''
    for item in lista:
        festacoes = festacoes + estacoes[item] + ', '
    return festacoes


vendas = [
    # Gasolina
    [
        # OR CT OC MD
        [1, 2, 3, 5],  # Verão
        [4, 5, 6, 4],  # Outono
        [7, 8, 9, 3],  # Inverno
        [10, 11, 12, 2],  # Primavera
        [4, 3, 2, 1]  # Black Pride Month
    ],
    # Gasóleo
    [
        # OR CT OC MD
        [13, 14, 15, 5],  # Verão
        [16, 17, 18, 4],  # Outono
        [19, 20, 21, 3],  # Inverno
        [22, 23, 24, 2],  # Primavera
        [4, 3, 2, 1]  # Black Pride Month
    ],
    # Gas
    [
        # OR CT OC MD
        [25, 26, 27, 5],  # Verão
        [28, 29, 30, 4],  # Outono
        [31, 32, 33, 3],  # Inverno
        [34, 35, 36, 2],  # Primavera
        [4, 3, 2, 1]  # Black Pride Month
    ]
]

total = [
    # v, o, i, p estações
    [],
    # or, ct, oc grupos
    []
]
for a in range(len(vendas[0])):
    total[0].append(0)
for a in range(len(vendas[0][0])):
    total[1].append(0)
estacoes = ['Verão', 'Outono', 'Inverno', 'Primavera', 'Black Pride Month']
grupos = ['Oriental', 'Central', 'Ocidental', 'Madeira']
totaltotal = 0
# x = 2/3
# y = 4/5
# z = 3/4
for x in range(len(vendas)):
    for y in range(len(vendas[0])):
        for z in range(len(vendas[0][0])):
            for t in range(len(total[0])):
                if y == t:
                    total[0][t] += vendas[x][y][z]
            for t in range(len(total[1])):
                if z == t:
                    total[1][t] += vendas[x][y][z]
            totaltotal += vendas[x][y][z]

print(f'Total de tudo é {totaltotal}')
print('----------------------------------')
for t in range(len(total[0])):
    print(f'Total no {estacoes[t]} é {total[0][t]}')

print('----------------------------------')
for t in range(len(total[1])):
    print(f'Total do {grupos[t]} {total[1][t]}')

print('----------------------------------')
maior = 0
maiores = 0
lmaiores = []
for e in range(len(total[0])):
    if total[0][e] > maior:
        maior = total[0][e]
        maiores = e
        lmaiores = [maiores]
    elif total[0][e] == maior:
        lmaiores.append(e)
if len(lmaiores) > 1:
    print(f'As estaçõe com mais vendas são {fmaiores(lmaiores)}com {total[0][lmaiores[0]]} de vendas')
else:
    print(f'A estação com mais vendas é {estacoes[maiores]} com {maior} de vendas')

menor = total[1][0]
menores = 0
lmenores = [menores]
for e in range(len(total[1])):
    if total[1][e] < menor:
        menor = total[1][e]
        menores = e
        lmenores = [menores]
    elif total[1][e] == menor:
        lmenores.append(e)
if len(lmenores) > 1:
    print(f'As estaçõe com mais vendas são {fmaiores(lmenores)}com {total[1][lmenores[0]]} de vendas')
else:
    print(f'O grupo com menos vendas é o {grupos[menores]} com {menor} de vendas')
