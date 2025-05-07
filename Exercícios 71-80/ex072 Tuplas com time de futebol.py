times = ('Flamengo', 'Internacional', 'Atlético MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
        'Santos', 'Athlético PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético GO',
         'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print('\n5 PRIMEIROS COLOCADOS: ', end=' ')
for c in range(0, 5):
    print(f'{c+1}º{times[c]}', end=' ')

print('\n4 ULTIMOS COLOCADOS: ', end=' ')
for i in range(0, 4):
    print(f'{i+17}º{times[i + 16]}', end=' ')

print()
print(f'Times em ordem alfabética: {sorted(times)}')

print('Posição BRAGANTINO: O Bragantino está na {}º posição.'.format(times.index('Bragantino') + 1))