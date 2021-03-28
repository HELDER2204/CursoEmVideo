n = str(input('Digite sua expressão: '))
cont = 0
cont2 = 0
if n in '(':
    cont += 1
if n in ')':
    cont2 += 1
if cont == cont2:
    print('Sua expressão é valida.')
else:
    print('Sua expressão é invalida.')

exp = str(input('Digite sua expressão: '))
pilha = list()
for simb in exp:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida.')
else:
    print('Sua expressão é invalida.')

