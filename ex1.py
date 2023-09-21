# Escreve um programa que tem 4 funções:
# somar
# subtrair
# dividir
# multiplicar
def aritmetica(op, num1, num2):
    if op.lstrip().rstrip() == "+":
        resultado = num1 + num2
    elif op.lstrip().rstrip() == "-":
        resultado = num1 - num2
    elif op.lstrip().rstrip() == "*":
        resultado = num1 * num2
    elif op.lstrip().rstrip() == "/":
        resultado = num1 / num2
    else:
        resultado = "Operação não existe."
    return resultado


def contas(op, num1, num2):
    if op == "+":
        resultado = num1 + num2
    else:
        if op == "-":
            resultado = num1 - num2
        else:
            if op == "*":
                resultado = num1 * num2
            else:
                if op == "/":
                    resultado = num1 / num2
                else:
                    resultado = "Operação inválida"
    return resultado


def continhas(op, n1, n2):
    resultado = "Operação invalida"
    if op == '+':
        resultado = n1 + n2
    if op == '-':
        resultado = n1 - n2
    if op == '*':
        resultado = n1 * n2
    if op == '/':
        resultado = n1 / n2
    return resultado


a = 10
b = 15

print(aritmetica('+', a, b))
print(aritmetica('-', a, b))
print(aritmetica('*', a, b))
print(aritmetica('/', a, b))
print(aritmetica('blah', a, b))
print('--------')
print(contas('+', a, b))
print(contas('-', a, b))
print(contas('*', a, b))
print(contas('/', a, b))
print(contas('blah', a, b))
print('--------')
print(continhas('+', a, b))
print(continhas('-', a, b))
print(continhas('*', a, b))
print(continhas('/', a, b))
print(continhas('blah', a, b))

(print(type(a)))
op = input("Insira a operação que quer: +, -, *, / : ")
print(f"{a} {op} {b} = {aritmetica(op, a, b)}")
