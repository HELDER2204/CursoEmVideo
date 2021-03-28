palavras = ('Abacate', 'Leite', 'Garrafa', 'Fone', 'Saúde', 'Livro', 'Panfleto', 'Carregador', 'Mascote')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos:', ' ', end='')
    for letra in c:
        if letra in 'ÁáaAÉEéeÍIiÓOóoÚUúu':
            print(letra.lower(), ' ', end='')


