# 16. Escreva um programa que lê um número e cria uma capicua cuja primeira
# metade é o número lido. Por exemplo:
# Escreva um número
# -> 347
# 347743
num = input('-> ')
x = len(num) * 2
y = 0
trocar = True
numero = 0
while x >= 0:
    numero = numero + (num[y] * (10 ** x))
    if y == len(num) - 1:
        trocar = False
    if trocar:
        y += 1
    else:
        y -= 1
    x -= 1
print(numero)
