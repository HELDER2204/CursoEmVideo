times = ('Flamengo', 'Internacional', 'Atlêtico-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Atlêtico-PR', 'Bragantino', 'Ceara SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza',
         'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
primeiro = times[0:4]
ultimos = times[-4:]
ordem = (sorted(times))
flu = times[4]
print('-='*100)
print(f'Os 4 primeiros times são: {primeiro}')
print('-='*100)
print(f'Os 4 últimos times são: {ultimos}')
print('-='*100)
print(f'Os times em ordem alfabética são:{ordem}')
print('-='*100)
print(f'O time do Fluminense esta em {times.index("Fluminense")+1}º lugar')
print('-='*100)
print('-'*80, 'FIM', '-'*200)