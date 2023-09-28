# 2x3x4
vendasx = [
    # Gasolina
    [
        #V  O  I   P
        [1, 4, 7, 10],  # OR
        [2, 5, 8, 11],  # CT
        [3, 6, 9, 12]  # OC
    ],
    # Gasóleo
    [
        # V   O   I   P
        [13, 16, 19, 22],  # OR
        [14, 17, 20, 23],  # CT
        [15, 18, 21, 24]  # OC
    ]
]
# 2x4x3
vendas = [
    # Gasolina
    [
        # OR CT OC
        [1, 2, 3],  # Verão
        [4, 5, 6],  # Outono
        [7, 8, 9],  # Inverno
        [10, 11, 12]  # Primavera
    ],
    # Gasóleo
    [
        # OR CT OC
        [13, 14, 15],  # Verão
        [16, 17, 18],  # Outono
        [19, 20, 21],  # Inverno
        [22, 23, 24]  # Primavera
    ]
]
# 3x2x4
# 3x4x2
# 4x2x3
# 4x3x2

print(f'Comprimento da lista vendas = {vendas[1][1][2]}')
total1 = 0

for x in range(len(vendas)):
    total2 = 0
    for z in range(len(vendas[0][0])):
        total3 = 0
        for y in range(len(vendas[0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f'total3 = {total3}')
    print(f'total2 = {total2}')
print(f'Total de Vendas = {total1}')
