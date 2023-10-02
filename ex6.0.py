nome = input('Qual é o seu nome? ')
num = int(input('Escolhe um numero: '))
y = num
x = num

while y - 1 > 0:
    x = x * (y - 1)
    y -= 1

if num == 0 or num == 1:
    x = 1
print(f'{nome}, o valor fatorial de {num} é {x}')
