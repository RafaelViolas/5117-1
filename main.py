"""
O meu hello world program
"""


def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


def mostrar(informacao):
    print(informacao)


width = 10
height = 20

perimeter = 2 * (width + height)
print("Perimeter = ", perimeter)

area = multiplicar(width, height)
mostrar(f"Area = {area}")



