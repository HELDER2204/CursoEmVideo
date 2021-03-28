lista = [[], []]
for l in range(1, 8):
    n = (int(input(f'Digite o {l}º valor:')))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 != 0:
        lista[1].append(n)
print(f'Os valores ínpares digitados foram: {sorted(lista[1])}')
print(f'Os valores pares digitados foram: {sorted(lista[0])}')



