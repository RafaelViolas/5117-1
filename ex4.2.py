import random


def ordenar(lista, ordem=1):
    troquei = True

    while troquei:
        x = 0
        troquei = False
        while x < len(lista) - 1:
            if lista[x] * ordem > lista[x + 1] * ordem:
                y = lista[x + 1]
                lista[x + 1] = lista[x]
                lista[x] = y
                troquei = True
            x += 1
    return lista


if __name__ == '__main__':
    vendas = []
    for x in range(5):
        vendas.append(random.randint(0, 100))
    print(ordenar(vendas))
    print(ordenar(vendas, -1))
