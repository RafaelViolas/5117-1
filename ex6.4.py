# receber texto = ''
# quantas vezes aparece cada letra?
# apresenta do maior para o menor
def ordenar(listavalues, listakeys, ordem=1):
    troquei = True

    while troquei:
        x = 0
        troquei = False
        while x < len(listavalues) - 1:
            if listavalues[x] * ordem > listavalues[x + 1] * ordem:
                y = listavalues[x + 1]
                listavalues[x + 1] = listavalues[x]
                listavalues[x] = y
                y = listakeys[x + 1]
                listakeys[x + 1] = listakeys[x]
                listakeys[x] = y
                troquei = True
            x += 1
    for z in range(len(listavalues)):
        letras[listakeys[z]] = listavalues[z]
    return letras


texto = input('Insira um texto: ')
dicionario = {}
letras = {}
for l in texto:
    dicionario[l] = 0
for t in texto:
    dicionario[t] += 1

print(dicionario)

dckeys = []
dcvalues = []
for x in dicionario.values():
    dcvalues.append(x)
for x in dicionario.keys():
    dckeys.append(x)

print(ordenar(dcvalues, dckeys, -1))
