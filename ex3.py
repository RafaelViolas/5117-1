from utilitarios import aritmetica

if __name__ == '__main__':  # obriga o codigo a começar aqui
    nome = input('Como te chamas? ')
    continuar = 's'
    while continuar == 's':
        fator1 = float(input('Insira o primeiro número '))
        fator2 = float(input('Insira o segundo número '))
        operacao = input('Insira a operação [+ , -, :, *] ')
        print(f'Olá {nome}, {fator1} {operacao} {fator2} = {aritmetica(fator1, fator2, operacao)}')
        continuar = input('Repetir [s | n]? ')
    print(f'Adeus {nome}!')
