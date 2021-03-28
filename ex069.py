cont18 = contM20 = homem = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo: [M/F]? ')).upper().strip()

    perg = ' '
    while perg not in 'SN':
        perg = str(input('Você quer contiuar: [S/N]? ')).upper().strip()

    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        contM20 += 1
    if perg == 'N':
        break
print(f'Temos um total de {cont18} pessoas maiores de 18 anos.')
print(f'Temos um total de {homem} homens')
print(f'Temos um total de {contM20} mulheres menores de 20 anos')

