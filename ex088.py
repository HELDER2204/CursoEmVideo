from random import sample
from time import sleep
print('-'*33)
print('            MEGA-SENA')
print('-'*33)
jogos = int(input('Quantos jogos você quer sortear? '))
print(f"-=-=-=-=Sorteando {jogos} jogos-=-=-=-=")
for c in range(1, jogos + 1):
    sorteio = sample(range(1, 61), 6)
    print(f'Jogo {c}: {sorteio}')
    sleep(0.5)

