while True:
    valor = int(input('Você quer saber o valor de qual tabuada?'))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {valor} = {c * valor}')
print('Fim')
