conj = dict()
conj['nome'] = str(input('Nome: '))
conj['média'] = float(input('Média: '))
print('-='*30)
print(f'Nome é igual a {conj["nome"]} ')
print(f'Média é igual a {conj["média"]}')
if conj['média'] < 5:
    print('Situação é igual a reprovado.')
elif conj['média'] < 7:
    print('Situação é igual a recuperação.')
else:
    print('Situação é igual a aprovado')

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')