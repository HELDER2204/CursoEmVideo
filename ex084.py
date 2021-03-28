lista = list()
dados = list()
mais = menos = 0
while True:
    dados.append(str(input('Seu nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        mais = menos = dados[1]
    else:
        if dados[1] > mais:
            mais = dados[1]
        if dados[1] < menos:
            menos = dados[1]
    lista.append(dados)
    dados.clear()
    resp = str(input('Você que continuar? [S/N] ')).strip()
    if resp in 'Nn':
            break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi {mais}', end='')
for p in lista:
    if p[1] == mais:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menos}', end='')
for p in lista:
    if p[1] == menos:
        print(f'[{p[0]}]', end='')



