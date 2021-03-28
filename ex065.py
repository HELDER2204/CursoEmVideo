resp = 's'
valor = soma = cont = div = menor = maior = 0
while resp in 'Ss':
    valor = int(input('Digite um valor:'))
    soma += valor
    cont += 1
    div = soma / cont
    if cont == 1:
        maior = menor = valor
    else:
        if valor < menor:
         menor = valor
        if valor > maior:
         maior = valor
    resp = str(input('Você quer continuar? [S/N] ')).strip()
print('Você digitou {} números e a média deles é {:.2f}'.format(cont, div))
print('O menor valor digitado foi {} e o maior foi {}'.format(menor, maior))

