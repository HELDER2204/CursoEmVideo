tot = 0
jogador = dict()
gol = list()
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
jogador['Gols'] = 0
for c in range(1, jogador['Partidas']+1):
    gol.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['Total de gols'] = sum(gol)
jogador['Gols'] = gol[:]
print('-='*30)
print(jogador)
print('-='*30)
for i, v in jogador.items():
    print(f'O campo {i} tem valor {v}')
print('-='*30)
for i, v in enumerate(gol):
    print(f' => Na partida {i+1}, fez {v} gol(s)')
print(f'Foi um total de {jogador["Total de gols"]} gols')
