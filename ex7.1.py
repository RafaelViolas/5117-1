# 15. Escreva um programa que lê uma série de dígitos (terminando com -1) e
# calcula o inteiro que tem esses dígitos. Por exemplo, lendo os dígitos 1 5
# 4 5 8 -1, calcula o número inteiro 15458.
# 10 ^ n elemento da lista
lista = []
num = 0
while num != -1:
    num = int(input('Escreve uma série de numeros que termine com "-1": '))
    if num == -1:
        break
    else:
        lista.append(num)
print(lista)
x = 0
y = len(lista)
numero = 0
while x < len(lista):
    numero = numero + lista[x] * (10 ** (y - 1))
    x += 1
    y -= 1
print(numero)
