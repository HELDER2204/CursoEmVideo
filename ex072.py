ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valor = int(input('Digite um valor de 0 a 20: '))
    if valor < 0 or valor > 20:
        print('Número inválido. Digite um número de 0 a 20')
    else:
        break
print(f'O valor digitado, por extenso é: {ext[valor]}.')
