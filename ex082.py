lista = list()
par = list()
inpar = list()
while True:
    n = (int(input('Digite uma valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 != 0:
        inpar.append(n)
    resp = str(input('Você quer continuar? [S/N] ')).strip()
    if resp in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista com os números pares é {par}')
print(f'A lista com os números ínpares é {inpar}')
