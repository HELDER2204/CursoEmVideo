from time import sleep
primeiro = float(input('Digite o 1º valor: '))
segundo = float(input('Digite o 2º valor: '))
opção = 0
sairPrograma = 5
while opção != sairPrograma:
    print('[1] somar\n[2] multiplicar\n[3] Maior\n[4] novos números\n[5] Sair do programa')
    print('-='*12)
    opção = int(input('>>>>> Digite sua opção: '))
    if opção == 1:
        print('A soma entre {} + {} é {}.'.format(primeiro, segundo, primeiro + segundo))
    if opção == 2:
        print('A multiplicação entre {} e {} é igual: {}'.format(primeiro, segundo, primeiro * segundo))
    if opção == 3:
        if primeiro > segundo:
            print('O maior número entre {} e {} é {}'.format(primeiro, segundo, primeiro))
        if segundo > primeiro:
            print('O maior número entre {} e {} é {}'.format(primeiro, segundo, segundo))
    if opção == 4:
        primeiro = float(input('Digite o 1º valor: '))
        segundo = float(input('Digite o 2º valor: '))
        print('[1] somar\n[2] multiplicar\n[3] Maior\n[4] novos números\n[5] Sair do programa')
        opção = int(input('Digite sua opção: '))
    if opção > 5:
        print('Opção inválida. Tente novamente.')
print('FiNALIZANDO...')
sleep(2)
print('Fim do programa')




