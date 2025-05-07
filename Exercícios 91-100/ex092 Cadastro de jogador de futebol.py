cadastro = dict()
gols = list()

cadastro['nome'] = input('Nome do jogador: ')
cadastro['gols'] = gols

partidas = int(input(f'Quantas partidas jogou {cadastro["nome"]}? '))

for i in range(1, partidas+1):
	gols.append(int(input(f'Quantos gols na partida {i}? ')))

print(f'\nMuito prazer, {cadastro["nome"]}.')
print(f'{cadastro["nome"]} fez em cada uma das {partidas} partidas {cadastro["gols"]}.')
print(f'{cadastro["nome"]} fez no total {sum(gols)} gols.')

print(f'\n{cadastro["nome"]} jogou {partidas} partidas.')
for i in range(1, partidas+1):
	print(f'=> Na partida {i}, fez {gols[i-1]}.')

print(f'Um total de {sum(gols)} gols.')

print('\nObrigado por utilizar nossos sistemas.')

