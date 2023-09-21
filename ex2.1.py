"""
Exercicio com lista
"""

lista = [10,20,20,15,5,60,140,80,40]
print(lista)

# Se o valor do elemento da lista é >= 20,
# então o valor do elemento da lista divido por 2
casa = 0
for n in lista:
    if(n >= 20):
        lista[casa] = n/2
    casa = casa + 1

print(lista)
#[10,(20 - erro),10,(7.5 - erro),5,30,70,40,20]