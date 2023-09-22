# Imprime a lista na ordem inversa

lista = [10, 20, 7, 4, 20]
atsil = []
y = len(lista) - 1
for x in range(len(lista)):
    print(lista[y - x])
    atsil.append(lista[y - x])
print(atsil)
