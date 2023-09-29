# Calcular Salário
# Perguntar nome
# Perguntar Horas int
# Horas: 0 - 40 Preco Normal
# Horas: 41 - 60 Preco x1.5
# Horas: >61 Preco x2
# Perguntar Preço hora double
# Perguntar vendeu
# Perguntar Seg Social = 11%(????)
# Vendas:
# 10000 / 20000 / 30000 / 40000 / infinito
#   1% /  2%   /   3%  /   4%  /     5%
# Ex:
# 25000
# 10000 1% 100
# 10000 2% 200
#  5000 3% 150
vvvendas = [
    [1000, 2000, 3000, 4000],
    [0.01, 0.02, 0.03, 0.04, 0.05]
]
vvvvendas = []
e = 0
for v in range(len(vvvendas[0])):
    e += vvvendas[0][0] * vvvendas[1][v]
    vvvvendas.append(e)

precoporhora = [[1, 1.5, 2], [40, 60]]
valordecasadepreco = 0

nome = input('Qual é o seu nome? ')
horas = int(input('Quantas horas trabalha? '))
if horas <= precoporhora[1][0]:
    valordecasadepreco = 0
elif precoporhora[1][0] < horas <= precoporhora[1][1]:
    valordecasadepreco = 1
elif horas > precoporhora[1][1]:
    valordecasadepreco = 2
preco = float(input('Quanto ganha por hora? '))
vendas = int(input('Quantas vendas obteve? '))
segsocial = float(input('Quanto é que é a sua Segurança Social(1% == 0.01) '))

vvendas = 0
if vvvendas[0][0] < vendas <= vvvendas[0][1]:
    vvendas = (vendas - vvvendas[0][0]) * vvvendas[1][1]
    vvendas += vvvvendas[0]
elif vvvendas[0][1] < vendas <= vvvendas[0][2]:
    vvendas = (vendas - vvvendas[0][1]) * vvvendas[1][2]
    vvendas += vvvvendas[1]
elif vvvendas[0][2] < vendas <= vvvendas[0][3]:
    vvendas = (vendas - vvvendas[0][2]) * vvvendas[1][3]
    vvendas += vvvvendas[2]
elif vendas > vvvendas[0][3]:
    vvendas = (vendas - vvvendas[0][3]) * vvvendas[1][4]
    vvendas += vvvvendas[3]
else:
    vvendas = vendas * vvvendas[1][0]

salario = horas * (preco * precoporhora[0][valordecasadepreco]) + vvendas
precosegsocial = salario * segsocial

print(f'Olá {nome}')
print(f'Trabalhas {horas} ganhando {preco} a hora.')
print(f'Ganhando assim {horas * (preco * precoporhora[0][valordecasadepreco])}')
print(f'Vendeu {vendas} dos quais {vvendas} recebeu')
print(f'Com Segurança Social de {segsocial} descontando {precosegsocial.__round__(2)} ')
print(f'Recebe em Liquido: {(salario - precosegsocial).__round__(2)} ')
