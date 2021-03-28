from random import randint
from time import sleep
from operator import itemgetter
jogador = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
print('Valores sorteados.')
for i, v in jogador.items():
    print(f'{i} tirou {v} no dado.')
    sleep(0.5)
print('-='*30)
print('== Ranking dos jogadores ==')
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)


