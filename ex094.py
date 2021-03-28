principal = list()
dados = dict()
dados2 = list
tot = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M OU F.')
    dados['idade'] = int(input('Idade: '))
    tot += dados.copy()['idade']
    principal.append(dados.copy())
    dados2 = dados.copy()
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
média = tot / len(principal)
print(f'A) Ao todo temos {len(principal)} pessoas cadastradas.')
print(f'B) A média de idade é de {média:.2f}.')
print('C) As mulheres cadastradas foram ', end='')
for p in principal:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('D) As pessoas acima da média são: ')
for p in principal:
    if p['idade'] >= média:
        print('        ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

