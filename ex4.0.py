"""
1 - Cria uma lista com nomes das Ilhas
2 - Pede valores para cada ilha
3 - Apresenta: total
             : valor minimo e ilhas com esse valor
             : valor maximo e ilhas com esse valor
             : Ordena de forma crescente
             : Ordena de forma decrescente
"""

Ilhas = ['Terceira', 'Graciosa', 'São Jorge', 'Faial', 'Pico']
vendas = [0, 0, 0, 0, 0]
total = 0
maior = 0
menor = 0
# icmv = Ilhas com maiores valores
icmv = []
# icmnv = Ilhas com menores valores
icmnv = []
# crescente
crescente = []
# descrescente
decrescente = []
for x in range(len(vendas)):
    vendas[x] = float(input(f'Insira as vendas para {Ilhas[x]}: '))

for v in vendas:
    total = total + v
print(f'O total de vendas de todas as Ilhas é {total}')

for y in range(len(vendas)):
    if vendas[y] > vendas[maior]:
        maior = y
        icmv = []
    if vendas[y] == vendas[maior]:
        icmv.append(y)
    if vendas[y] < vendas[menor]:
        menor = y
        icmnv = []
    if vendas[y] == vendas[menor]:
        icmnv.append(y)

print(f'a maior venda é {vendas[maior]} e foi da Ilha {Ilhas[maior]}')
for n in icmv:
    if n != maior:
        print(f'A Ilha {Ilhas[n]} também atingiu o maior valor de vendas')
print(f'a menor venda é {vendas[menor]} e foi da Ilha {Ilhas[menor]}')
for n in icmnv:
    if n != menor:
        print(f'A Ilha {Ilhas[n]} também atingiu o menor valor de vendas')

troquei = True

while troquei:
    x = 0
    y = 0
    troquei = False

    while x < len(vendas) - 1:
        if vendas[x] > vendas[x + 1]:
            y = vendas[x + 1]
            vendas[x + 1] = vendas[x]
            vendas[x] = y
            troquei = True
        x += 1
print(vendas)
# 4 5 1 2 3
