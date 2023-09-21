"""
Exercicio com lista
"""

lista = [10,20,20,15,5,60,140,80,40]
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
    if n >= 0 and n <= 10:
        ZeroADez = ZeroADez + 1
    elif n >= 11 and n <= 20:
        OnzeAVinte = OnzeAVinte + 1
    elif n >= 21 and n <= 30:
        VinteEUmATrinta = VinteEUmATrinta + 1
    elif n >= 31 and n <= 40:
        TrintaEUmAQuarenta = TrintaEUmAQuarenta + 1
    elif n >= 41 and n <= 50:
        QuarentaEUmACinquenta = QuarentaEUmACinquenta + 1
    elif n > 50:
        MaiorQueCinquenta = MaiorQueCinquenta + 1
    else:
        print(f'O Numero {n} é menor que 0')

print(f'Quantidade de numeros entre 0 a 10 é {ZeroADez}')
print(f'Quantidade de numeros entre 11 a 20 é {OnzeAVinte}')
print(f'Quantidade de numeros entre 21 a 30 é {VinteEUmATrinta}')
print(f'Quantidade de numeros entre 31 a 40 é {TrintaEUmAQuarenta}')
print(f'Quantidade de numeros entre 41 a 50 é {QuarentaEUmACinquenta}')
print(f'Quantidade de numeros maior que 50 é {MaiorQueCinquenta}')
