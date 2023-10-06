pessoas = []
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['telefone'] = input('Telefone: ')
    pessoas.append(pessoa.copy())
    if input('Deseja inserir mais uma pessoa? ') not in ('s', 'sim'):
        break

print('--- Usando for ---')

for x in pessoas:
    print(f"{x['nome']} tem {x['idade']} e o seu telefone é {x['telefone']}")

print('--- Usando for com range ---')
for x in range(len(pessoas)):
    print(f"{pessoas[x]['nome']} tem {pessoas[x]['idade']} e o seu telefone é {pessoas[x]['telefone']}")

print('--- Usando while ---')
x = 0
while x < len(pessoas):
    print(f"{pessoas[x]['nome']} tem {pessoas[x]['idade']} e o seu telefone é {pessoas[x]['telefone']}")
    x += 1
