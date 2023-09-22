"""
Este programa implementa funções aritméticas
"""


def aritmetica(valor1, valor2, op='+'):
    """
    Esta função implementa as operações de somar, subtrair, multiplicar e dividir
    :param valor1: Primeiro fator da operação
    :param valor2: Segundo fator da operação
    :param op: Operação; valores válidos são; + - : *
    :return: Resultado da operação
    """
    total = 'Código de operação inválido'
    if op == '+':
        total = valor1 + valor2
    if op == '-':
        total = valor1 - valor2
    if op == ':':
        total = valor1 / valor2
    if op == '*':
        total = valor1 * valor2

    return total
