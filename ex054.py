from datetime import date
totmax = 0
totmin = 0
for c in range(1, 8):
    pessoa = int(input('Qual a data de nascimento da {}º pessoa?'.format(c)))
    idade = date.today().year - pessoa
    if idade < 18:
        totmin += 1
    else:
        totmax += 1
print('Temos {} pessoas menores de idade'.format(totmin))
print('Temos {} pessoas maiores de idade'.format(totmax))

'''from datetime import date
n1 = int(input('Data de nascimento da 1º pessoa'))
n2 = int(input('Data de nascimento da 2º pessoa'))
n3 = int(input('Data de nascimento da 3º pessoa'))
n4 = int(input('Data de nascimento da 4º pessoa'))
n5 = int(input('Data de nascimento da 5º pessoa'))
n6 = int(input('Data de nascimento da 6º pessoa'))
n7 = int(input('Data de nascimento da 7º pessoa'))
for c in range(n1, n7 + 1, 1):
    idade = data - c
    print(idade)'''
