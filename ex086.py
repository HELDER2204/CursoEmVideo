lista1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista1[l][c] = (int(input(f'Digite um valor para[{l}, {c}]:')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista1[l][c]:^5}]', end='')
    print()

