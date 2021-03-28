from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10), randint(1, 10))
print('Os números gerados são: ', end='')
for c in num:
    print(c, '', end='')
print(f'\nO maior número: {max(num)}')
print(f'O menor número: {min(num)}')