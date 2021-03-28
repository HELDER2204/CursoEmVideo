valor = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado.')
    else:
        print('Número já adionado, tente outro número.')
    não = str(input('Você quer continuar? [S/N]? ')).strip()
    if não in 'Nn':
            break
valor.sort()
print(valor)
