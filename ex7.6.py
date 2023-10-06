soma = 1
denominador = 1
print("Qual o valor de x")
x = int(input("? "))
soma += x
print("Qual o valor de n")
n = int(input("? "))

ultimoTermo = x
for pos in range(2, n + 1):
    ultimoTermo = ultimoTermo * x / pos
    soma += ultimoTermo

print("O valor da soma é ", soma)
# x = 3
# soma = 4
# n = 5
#
# 3 = 3 * 3/2 # 1,5
# 4 += 4,5
# 4,5 = 4,5 * 3/3 # 1
# 8,5 += 4,5
# 4,5 = 4,5 * 3/4 # 0.75
# 13 += 3,375
# 3,375 = 3,375 * 3/5 # 0.6
# 16,375 += 2,025
# 18,4
