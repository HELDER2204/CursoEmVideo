tot = maisde = maisbarato = cont = 0
nomebarato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    tot += preço
    cont += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar: [S/N] ? ')).strip().upper()
    if cont == 1:
        maisbarato = preço
        nomebarato = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
            maisbarato = produto
    if preço > 1000:
        maisde += 1
    if resp == 'N':
        break
print(f'Foi gasto um total de R$: {tot}.')
print(f'Ao todo tivemos {maisde} acima de R$: 1000,00.')
print(f'O produto mais barato foi {nomebarato}.')


