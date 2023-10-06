# ex 20
res = ""
for n in range(1, 10):
    const = 8
    res = res + str(n)
    print(f'{int(res)} x {const} + {n} = {int(res) * const + n}')
