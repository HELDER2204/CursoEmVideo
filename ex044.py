cp = float(input('Valor das compras:'))
print('''
[ 1 ] Dinheiro/Cheque
[ 2 ] Cartão a vista
[ 3 ] 2x cartão
[ 4 ] 3x ou mais''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('O valor da sua compra será: R${} '.format(cp / 100 * 90))
elif opcao == 2:
    print('O valor da sua compra será: R${} '.format(cp / 100 * 95))
elif opcao == 3:
    print('O valor da sua compra será: R${} '.format(cp))
elif opcao == 4:
    print('O valor da sua compra será: R${} '.format(cp / 100 * 120))
else:
    print('Opção inválida')