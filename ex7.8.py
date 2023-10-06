# Pergunta quantos?
# Pergunta Inicio?
# Pergunta Fim?
# Sorteia entre o inicio e fim a quantidade
import random

# Apresenta: Os Numeros
# quantos pares
# quantos impares
# quantos primos

quantidade = int(input('Quantos? '))
inicio = int(input('Começa em? '))
fim = int(input('Acaba em? '))
if inicio > fim:
    print('O fim precisa de ser maior que o inicio')
else:
    lista = []
    for x in range(quantidade):
        lista.append(random.randint(inicio, fim))
    pares = 0
    listapares = []
    impares = 0
    listaimpares = []
    primos = 0
    listaprimos = []
    print(f'Lista dos numeros: {lista}')
    for y in lista:
        if y % 2 == 0:
            pares += 1
            listapares.append(y)
        else:
            impares += 1
            listaimpares.append(y)
        test = 0
        for x in range(1, y + 1):
            if y % x == 0:
                test += 1
        if test == 2:
            primos += 1
            listaprimos.append(y)
    print(f'Quantidade de numeros pares: {pares} com valores {listapares}')
    print(f'Quantidade de numeros impares: {impares} com valores {listaimpares}')
    print(f'Quantidade de numeros primos: {primos} com valores {listaprimos}')
