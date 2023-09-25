semanas = [1, 2, 3, 4]
dias = ['segunda', 'terceira', 'quarta', 'quinta', 'sexta']
# Dias[x]
x = 0
y = 0
print(len(dias))
while x < len(semanas):
    y = 0
    while y < len(dias):
        print(f'Semana {semanas[x]} - {dias[y]}')
        y += 1
    x += 1
    print()
