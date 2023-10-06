# 18. Escreva um programa que lê um número inteiro e determina quantas vezes
# aparecem dois zeros seguidos. Por exemplo:
# Escreva um inteiro
# ? 98007640003
# O numero tem 3 zeros seguidos
numero = input('Escreva um inteiro \n? ')
ndezeros = 0
for n in range(len(numero) - 1):
    if numero[n] == '0' and numero[n + 1] == '0':
        ndezeros += 1
print(f'O numero tem {ndezeros} zeros seguidos')
