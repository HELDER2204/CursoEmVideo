valor = (int(input('Digite uma valor: ')), int(input('Digite uma valor: ')), int(input('Digite uma valor: ')),
         int(input('Digite uma valor: ')))
print(f'O número nove apareceu {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O número três, foi digitado na posição {valor.index(3)+1}')
else:
    print('O número 3 não foi digitado.')
print('os números pares são os  ', end='')
for c in valor:
    if c % 2 == 0:
        print(c, end='')
