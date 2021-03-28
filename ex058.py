from random import randint
aleatorio = randint(1, 10)
jogador = int(input('Digite uma número de 1 a 10: '))
vezes = 1
while aleatorio != jogador:
    vezes += 1
    if aleatorio > jogador:
        jogador = int(input('Eu pensei em um número maior... tente novamente:'))
    if aleatorio < jogador:
        jogador = int(input('Eu pensei em um número menor... tente novamente:'))
print('Você precisou jogar {} para acertar. Eu joguei {}. Você acertou, parabéns!!!'.format(vezes, aleatorio))
