lista = []
num = 0
while num != -1:
    num = int(input('Escreva um dígito\n(-1 para terminar) \n? '))
    if num == -1:
        break
    else:
        lista.append(num)
x = 0
y = len(lista)
numero = 0
while x < len(lista):
    numero = numero + lista[x] * (10 ** (y - 1))
    x += 1
    y -= 1
print(f'O número é: {numero}')
