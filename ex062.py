print('Contador de P.A')
print('=-='*5)
n1 = int(input('Primeiro termo:'))
n2 = int(input('Razão:'))
cont = 1
termo = n1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('{} termos utilizados'.format(total))






