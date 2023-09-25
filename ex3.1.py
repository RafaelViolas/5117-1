# Cria uma lista com os nomes das ilhas do grupo Central

Ilhas = ['Terceira', 'Graciosa', 'São Jorge', 'Faial', 'Pico']

# Cria uma lista com 5 casas, Inicializadas a 0
vendas = [0, 0, 0, 0, 0]
total = 0

# Pede ao Utilizador para inserir vendas Para Cada Ilha
# "Insira as vendas para Terceira"
for x in range(len(vendas)):
    vendas[x] = float(input(f'Insira as vendas para {Ilhas[x]}: '))
# Apresenta:
# Total de Vendas

for v in vendas:
    total = total + v
print(f'O total de vendas de todas as Ilhas é {total}')

for x in range(len(vendas)):
    print(f'A Ilha {Ilhas[x]} vendeu {vendas[x]}')

# Média
# Ilha(s) e montante que venderam mais
# Ilha(s) e montante que venderam menos
# Ilha(s) e montante que venderam mais que a média
# Ilha(s) e montante que venderam menos que a média

total = 0
maior = 0
menor = 0

for n in range(len(vendas)):
    total = total + vendas[n]

print(f'blah blah {total / len(vendas)}')

for y in range(len(vendas)):
    if vendas[y] > vendas[maior]:
        maior = y
    if vendas[y] < vendas[menor]:
        menor = y
    if vendas[y] > total / len(vendas):
        print(f'numero {vendas[y]} é maior que a media e foi da Ilha {Ilhas[maior]}')
    else:
        print(f'numero {vendas[y]} é menor que a media e foi da Ilha {Ilhas[menor]}')

print(f'a maior venda é {vendas[maior]} e foi da Ilha {Ilhas[maior]}')
print(f'a menor venda é {vendas[menor]} e foi da Ilha {Ilhas[menor]}')
