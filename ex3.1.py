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
#Ilha(s) e montante que venderam mais
#Ilha(s) e montante que venderam menos
#Ilha(s) e montante que venderam mais que a média
#Ilha(s) e montante que venderam menos que a média
