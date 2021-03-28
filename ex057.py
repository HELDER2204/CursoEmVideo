sexo = str(input('Digite seu sexo: [F/M] ')).upper().strip()
while sexo not in 'FfMm':
    sexo = str(input('Dados incorretos, digite novamente')).strip().upper()
print('Sexo {}, registrado com sucesso'.format(sexo))


