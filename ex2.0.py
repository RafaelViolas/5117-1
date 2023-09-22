"""
Exercicio com lista
"""

# 1. Crie uma lista vazia
lista = [70, 20, 30, 90, 50, 60, 10, 80, 40]

# total = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8]
# print(total)

total = 0
maior = 0
menor = 0
for n in range(len(lista)):
    total = total + lista[n]
    if lista[n] > lista[maior]:
        maior = n
    if lista[n] < lista[menor]:
        menor = n
    print(total)

print(f'O index do numero maior é {maior} e seu valor é {lista[maior]}')
print(f'O index do numero menor é {menor} e seu valor é {lista[menor]}')
print(total)

print("-----")
# 2. Adicione os elementos 1,2,3,4 e 5 usando append()
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.append(4)
# lista.append(5)

# 3. Imprima a lista
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

# 4 Agora, remova os elementos 3 e 6 (não esquecer de verificar se eles estão na lista)
if 3 in lista:
    lista.remove(3)
if 6 in lista:
    lista.remove(6)

# 5 Imprima a lista modificada
print(lista)
