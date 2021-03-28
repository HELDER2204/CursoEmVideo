menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}º pessoa?'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
            if peso > maior:
                maior = peso
print('O maior peso doi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))

