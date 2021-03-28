somaidade = 0
mediaidade = 0
homemvelho = 0
nomevelho = ''
totm = 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if c == 1 and sexo in 'mM':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
            homemvelho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
                totm += 1
print('A média de idade do grupo é de {}'.format(somaidade / 4))
print('O homem mais velho tem {} e o nome dele é {} '.format(homemvelho, nomevelho))
print('Temos o total de {} mulher (a) menores de 20 anos'.format(totm))
