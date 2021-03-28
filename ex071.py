valor = int(input('Valor à ser sacado R$: '))
c = 50
tot = valor
totc = 0
while True:
    if tot >= c:
        tot -= c
        totc += 1
    else:
        if totc > 0:
            print(f'Total de {totc} cédulas de R$: {c}')
        if c == 50:
            c == 20
        elif c == 20:
            c == 10
        elif c == 10:
            c == 1
        totc = 0
        if tot == 0:
            break
