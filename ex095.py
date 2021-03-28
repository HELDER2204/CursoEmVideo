jogador = dict()
partidas = list
gol = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas.append(int(input(f'Quantas partidas {jogador["nome"]} jogou? ')))
    for c in range(1, partidas):



