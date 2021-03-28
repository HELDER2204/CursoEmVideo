valor = list()
for c in range(1, 5):
    valor.append(int(input('Digite uma valor: ')))
print(f'O maior valor é {(max(valor))}. Ele está na posição {valor.index(max(valor)) + 1}.')
print(f'O menor valor é {(min(valor))}. Ele está na posição {valor.index(min(valor)) + 1}.')
           

