lista1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista1[l][c] = (int(input(f'Digite um valor para[{l}, {c}]:')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista1[l][c]:^5}]', end='')
        if lista1[l][c] % 2 == 0:
            par += lista1[l][c]
    print()
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    coluna3 += lista1[l][2]
print(f'A somada coluna 3 é {coluna3}')
for c in range(1, 3):
    if c == 0:
        maior = lista1[1][c]
    elif lista1[1][c] > maior:
        maior = lista1[1][c]
print(f'O maior valor da segunda linha é {maior}')

