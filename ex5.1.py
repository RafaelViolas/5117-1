vendas = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

tipos = ('Gasolina', 'Gasóleo')
ilhas = ('Terceira', 'Graciosa', 'São Jorge', 'Pico', 'Faial')

total = 0
for x in range(len(vendas)):
    totaltipo = 0
    for y in range(len(vendas[x])):
        totaltipo += vendas[x][y]
        # a) total += totaltipo
        # b) total += vendas[x][y]
    print(f'Total de vendas de {tipos[x]} = {totaltipo}')
    total += totaltipo
print(f'Total de vendas = {total}')

print()
total = 0
for y in range(len(vendas[0])):
    totaltipo = 0
    for x in range(len(vendas)):
        totaltipo += vendas[x][y]
        print(f'Total de vendas para {ilhas[y]} = {totaltipo}')
        total += totaltipo
    print(f' Total de Vendas = {total}')
