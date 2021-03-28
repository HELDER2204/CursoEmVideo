principal = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Primeira nota: ')))
    dados.append(float(input('Segunda nota: ')))
    resp = str(input('Quer continuar: [S/N]?  ')).strip()
    principal.append(dados[:])
    if resp in 'Nn':
        break
    dados.clear()
print('-='*30)
print(f'Nº:   NOME:    MÉDIA":     ')
print('-='*30)
for i, v, in enumerate(principal):
    media = (v[1] + v[2]) / 2
    print(f'{i:<4} {v[0]:<10} {media:>8.2f}')
while True:
    print('-'*40)
    resp2 = int(input('Mostrar notas de qual aluno (999 para interromper)?'))
    if resp2 == 999:
        break
    else:
        print(f'Notas de {principal[resp2][0]} são [{principal[resp2][1]}][{principal[resp2][2]}]')


