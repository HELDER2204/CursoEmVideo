n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))
n5 = int(input('Digite um número:'))
n6 = int(input('Digite um número:'))
soma = 0
for c in range(n1, n6+1):
    if c % 2 == 0:
        soma = soma + c
print('A soma dos números pares é: {}'.format(soma))