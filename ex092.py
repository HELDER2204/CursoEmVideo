from datetime import date
data = date.today().year
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip()
cadastro['Idade'] = data - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = float(input('Salário R$: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contratação'] + 35) - data
for i, v in cadastro.items():
    print(f'- {i} tem o valor {v}')




