# Imprime os elementos da lista e dizer se é par ou impar

lista = [10, 20, 7, 4, 20, 34, 55, 23, 11]

for n in lista:
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é impar')

print("------")

for n in range(len(lista)):
    if lista[n] % 2 == 0:
        print(f'{lista[n]} é par')
    else:
        print(f'{lista[n]} é impar')
