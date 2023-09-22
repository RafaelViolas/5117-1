lista = [10, 20, 20, 15, 5, 60, 140, 80, 40]

# Imprime no número de casas na lista
print(len(lista))

# Imprime a sequencia de numeros entre zero e o numero de casas na lista menos um
# Usa a variável x
for x in range(len(lista)):
    print(x)

print("-----")

# Imprime a sequência de números entre número de casas da lista menos um e zero.
# Usa a variável y
for y in range(len(lista)):
    print(len(lista) - (y+1))

