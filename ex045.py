from random import randint

print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
computador = randint(1, 3)
jogada = int(input('Digite sua opção: '))
if computador == jogada:
    print('Escolhemos a mesma coisa. Vamos jogar novamente.')
elif computador == 1 and jogada == 2:
    print('Eu escolhi pedra, você ganhou!')
elif computador == 1 and jogada == 3:
    print('Eu escolhi pedra, você perdeu!')
elif computador == 2 and jogada == 1:
    print('Eu escolhi papel, você perdeu!')
elif computador == 2 and jogada == 3:
    print('Eu escolhi papel, você ganhou!')
elif computador == 3 and jogada == 1:
    print('Eu escolhi tesoura, você ganhou!')
elif computador == 3 and jogada == 2:
    print('Eu escolhi tesoura, você perdeu!')
else:
    print('Opção invalida')


