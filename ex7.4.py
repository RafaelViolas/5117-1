# 5. Escreva um programa em Python que lê cinco números reais e calcula a
# sua média e o seu desvio padrão. A média, x ̄, e o desvio padrão,
# , de
#
# cinco números x1, ... x5 são dados respectivamente por:
# A primeira linha do seu programa deve ser from math import sqrt. Esta
# instrução importa a função sqrt que calcula a raiz quadrada. Por exemplo,
# sqrt(4) tem o valor 2.0.
from math import sqrt

x = 0
lista = []
while x < 5:
    lista.append(float(input(f'Introduz {5 - x} numeros reais: ')))
    x += 1
total = 0
for y in lista:
    total = total + y
media = total / len(lista)
total = 0
for z in lista:
    total = total + ((z - media) ** 2)
umquarto = total / 4
desviopadrao = sqrt(umquarto)

print(f'A media é {media}')
print(f'E o desvio padrão é {desviopadrao}')
