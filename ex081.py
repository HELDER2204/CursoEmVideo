n = list()
while True:
    n.append(int(input('Digite uma valor: ')))
    resp = str(input('Você quer continuar? [S/N] ')).strip()
    if resp in 'Nn':
        break
print(f'Foram ditados {len(n)} números. ')
print(f'os valores em ordem decrescente são: {sorted(n, reverse=True)} ')
if n.count(5):
    print(f'O valor 5  está contido na lista.')
else:
    print('O valor 5 não está contido na lista.')