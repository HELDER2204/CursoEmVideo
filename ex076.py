print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
lista = ('Lapis', 2.5, 'Boracha', 1.5, 'Mouse', 36.5, 'Biscoito', 4.5)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}', end='')
    else:
        print('R$:', lista[c])
