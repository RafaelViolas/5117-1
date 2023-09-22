"""
Exercicio com lista
"""

lista = [10, 20, 20, 15, 5, 60, 140, 80, 40]
listanumeros = [0, 0, 0, 0, 0, 0]
# entre 0-10
ZeroADez = 0
# entre 11-20
OnzeAVinte = 0
# entre 21-30
VinteEUmATrinta = 0
# entre 31-40
TrintaEUmAQuarenta = 0
# entre 41-50
QuarentaEUmACinquenta = 0
# entre >50
MaiorQueCinquenta = 0

for n in lista:
    if 0 <= n <= 10:
        ZeroADez += 1
        listanumeros[0] += 1
    elif 11 <= n <= 20:
        OnzeAVinte += 1
        listanumeros[1] += 1
    elif 21 <= n <= 30:
        VinteEUmATrinta += 1
        listanumeros[2] += 1
    elif 31 <= n <= 40:
        TrintaEUmAQuarenta += 1
        listanumeros[3] += 1
    elif 41 <= n <= 50:
        QuarentaEUmACinquenta += 1
        listanumeros[4] += 1
    elif n > 50:
        MaiorQueCinquenta += 1
        listanumeros[5] += 1
    else:
        print(f'O Numero {n} é menor que 0')

print(f'Quantidade de numeros entre 0 a 10 é {ZeroADez} ou {listanumeros[0]}')
print(f'Quantidade de numeros entre 11 a 20 é {OnzeAVinte} ou {listanumeros[1]}')
print(f'Quantidade de numeros entre 21 a 30 é {VinteEUmATrinta} ou {listanumeros[2]}')
print(f'Quantidade de numeros entre 31 a 40 é {TrintaEUmAQuarenta} ou {listanumeros[3]}')
print(f'Quantidade de numeros entre 41 a 50 é {QuarentaEUmACinquenta} ou {listanumeros[4]}')
print(f'Quantidade de numeros maior que 50 é {MaiorQueCinquenta} ou {listanumeros[5]}')
