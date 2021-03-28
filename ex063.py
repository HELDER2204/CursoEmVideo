termo = int(input('Quantos termos você quer mostrar? '))
primeiro = 0
segundo = 1
cont = 3
print('{} -> {}'.format(primeiro, segundo), end='')
while cont <= termo:
    terceiro = primeiro + segundo
    print(' -> {} '.format(terceiro), end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print('FIM')
