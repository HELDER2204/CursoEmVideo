soma = cont = 0
while True:
    valor = int(input('Digite um valor:'))
    print('Para para digite 999')
    soma += valor
    cont += 1
    if valor == 999:
        break
print(f'Você digitou {cont} números e soma deles é {soma}')
