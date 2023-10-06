# 5 ilhas
# utilizador da o nome das ilhas e a distancia a S miguel
# lista ilhas
# lista distancias
# ver a ilha que fica mais perto e a sua distancia
# ver a ilha que fica mais longe e a sua distancia
# Terceira, Graciosa, São Jorge, Faial e Pico
ilhas = []
distancias = []

for x in range(5):
    ilha = input('Insira o nome da ilha no grupo central: ')
    distancia = int(input(f'Insira a distancia de {ilha} a São Miguel: '))
    ilhas.append(ilha)
    distancias.append(distancia)

ilhamaisperto = ilhas[0]
distanciamaisperto = distancias[0]

ilhamaislonge = 0
distanciamaislonge = 0
for x in range(len(distancias)):
    if distancias[x] > distanciamaislonge:
        ilhamaislonge = ilhas[x]
        distanciamaislonge = distancias[x]

    if distancias[x] < distanciamaisperto:
        ilhamaisperto = ilhas[x]
        distanciamaisperto = distancias[x]
print(f'Ilha mais perto de S Miguel é {ilhamaisperto} com uma distancia de {distanciamaisperto}')
print(f'Ilha mais longe de S Miguel é {ilhamaislonge} com uma distancia de {distanciamaislonge}')
