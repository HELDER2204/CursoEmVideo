n1 = int(input('Primeiro termo:'))
n2 = int(input('Razão:'))
d = 9
for c in range(n1, d * n2, n2):
    print('{}'.format(c), end=' ->')
print('ACABOU!')
