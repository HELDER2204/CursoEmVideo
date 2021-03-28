print('Contador de P.A')
print('=-='*5)
n1 = int(input('Primeiro termo:'))
n2 = int(input('Razão:'))
cont = 1
termo = n1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += n2
    cont += 1
print('FIM')