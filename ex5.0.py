vendas = [
    [14, 18, 5, 140, 5, 1, 2, 3, 4, 5],
    [30, 52, 25, 15, 10, 1, 2, 3, 4, 5]
]
totalgasolina = 0
totalgasoleo = 0
ilhas = [
    [0, 0, 0, 0, 0],
    ['Terceira', 'Graciosa', 'Pico', 'Sjorge', 'Faial']
]

for x in range(len(vendas)):
    for y in range(len(vendas[x])):
        if x == 0:
            totalgasolina += vendas[x][y]
        elif x == 1:
            totalgasoleo += vendas[x][y]

i = 0
for i in range(len(vendas[i])):
    for z in range(len(ilhas)):
        if i < len(ilhas[0]):
            ilhas[0][i] = ilhas[0][i] + vendas[z][i]

print(f'Total de Vendas de gasolina = {totalgasolina}')
print(f'Total de Vendas de gasoleo = {totalgasoleo}')
print('------')

for v in range(len(ilhas[1])):
    print(f'Total de Vendas da ilha {ilhas[1][v]}  = {ilhas[0][v]}')
