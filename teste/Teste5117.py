"""
Nome completo: Rafael Machado Viola
"""


def correr_exercicio_1():
    print("A correr o exercício 1")
    print('Este programa determina qual de duas pessoas é a mais velha ou se têm a mesma idade.')
    nome1 = input('Como se chama a primeira pessoa? ')
    nome2 = input('Como se chama a segunda pessoa? ')
    idade1 = int(input(f'Qual é a idade de {nome1}? '))
    idade2 = int(input(f'Qual é a idade de {nome2}? '))
    if idade1 == idade2:
        print(f'{nome1} e {nome2} têm a mesma idade')
    elif idade1 > idade2:
        print(f'{nome1} é mais velho(a) que {nome2}')
    elif idade1 < idade2:
        print(f'{nome2} é mais velho(a) que {nome1}')


def correr_exercicio_2():
    print("A correr o exercício 2")
    clientes = [78, 25, 42, 61, 72]
    total = 0

    for x in clientes:
        total = total + x

    print(f'A soma de todos os clientes é {total}')


def correr_exercicio_3():
    print("A correr o exercício 3")
    clientes = [78, 25, 42, 61, 72]
    total = 0

    for x in range(len(clientes)):
        total = total + clientes[x]

    print(f'A soma de todos os clientes é {total}')


def correr_exercicio_4():
    print("A correr o exercício 4")
    clientes = [78, 25, 42, 61, 72]
    total = 0
    x = 0

    while x < len(clientes):
        total = total + clientes[x]
        x += 1

    print(f'A soma de todos os clientes é {total}')
    print(x)


if __name__ == '__main__':
    ex = input('Qual o exercício que deseja correr? [1-4]')

    try:
        ex = int(ex)
        if ex < 1 or ex > 4:
            raise ValueError('O exercício deve ser um número entre 1 e 4')
    except ValueError:
        raise ValueError('O exercício deve ser um número entre 1 e 4')

    # Create a dictionary that maps exercise numbers to functions
    exercise_functions = {
        1: correr_exercicio_1,
        2: correr_exercicio_2,
        3: correr_exercicio_3,
        4: correr_exercicio_4,
    }

    # Call the selected function based on the user's input
    exercise_functions[ex]()
