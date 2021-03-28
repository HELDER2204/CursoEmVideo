from random import randint
jogada2 = ''
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número de 1 a 10: '))
    jogada2 = str(input('Escolha par ou ímpar: [P/I] ')).upper().strip()[0]
    total = computador + jogador
    if total % 2 == 0 and jogada2 == 'P':
        cont += 1
        print(f'Você ganhou! Sua jogada foi {jogador} e o computador jogou {computador}. vamos jogar novamente!')
    if total % 2 != 0 and jogada2 == 'I':
        cont += 1
        print(f'Você ganhou! Sua jogada foi {jogador} e o computador jogou {computador}. Vamos jogar novamente!')
    if total % 2 == 0 and jogada2 == 'I':
        break
    if total % 2 != 0 and jogada2 == 'P':
        break
print('GAME OVER')
print(f'Você jogou {jogador} e o computador jogou {computador}.')
print(f'você perdeu!\nVocê teve um total de {cont} vitória (s).')
