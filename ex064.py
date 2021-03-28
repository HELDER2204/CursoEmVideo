cont = 0
soma = 0
valor = 0
valor = int(input('Digite um valor: '))
while valor != 999:
    soma += valor
    cont += 1
    valor = int(input('Digite um valor: '))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
print('Acabou')

