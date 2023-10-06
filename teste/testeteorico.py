vendas = [
    [
        [5, 18, 15],
        [6, 7, 14],
        [14, 17, 5]
    ],
    [
        [8, 10, 3],
        [15, 12, 14],
        [4, 13, 6]
    ]
]
total = 0
for x in range(len(vendas)):
    for y in range(len(vendas[x])):
        for z in range(len(vendas[x][y])):
            total += vendas[x][y][z]
    print(total)
print(total)
