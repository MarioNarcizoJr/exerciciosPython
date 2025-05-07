cadastro = dict()
gols = list()
artilharia = list()

condicao = 's'

while condicao != 'n':
	cadastro.clear()
	cadastro['nome'] = input('\nNome do jogador: ')
	partidas = int(input(f'\nQuantas partidas {cadastro["nome"]} jogou? '))
	gols.clear()
	for i in range(0, partidas):
		gols.append(int(input(f'     Quantos gols na partida {i+1}? ')))
	cadastro['gols'] = gols[:]
	cadastro['total'] = sum(gols)
	artilharia.append(cadastro.copy())
	condicao = input('\nDeseja continuar? [S/N] ').lower()
	while condicao not in 'sn':
		if condicao == 'sn':
			break
		print('Erro!, Digite apenas S ou N por favor!')

print(f'\n{"No."} ', end='')
for i in cadastro.keys():
	print(f'{i:<18}', end='')
print()
print('-'*50)
for i, v in enumerate(artilharia):
	print(f'{i:<4}', end='')
	for k in v.values():
		print(f'{str(k):<18}', end='')
	print()
print()

print('-'*50)

flag = int(input('Mostrar o dados de qual jogador? [999 para parar] '))

while flag != 999:
	if flag >= len(artilharia):
		print('Opção fora dos parâmetros, por favor tente novamente!')
	else:
		print(f'--> Levantamento do jogador {artilharia[flag]["nome"]}:')
		for i, g in enumerate(artilharia[flag]['gols']):
			print(f'     No jogo {i+1} fez {g} gols.')
	flag = int(input('Mostrar o dados de qual jogador? [999 para para] '))

print('\nObrigado por utilizar nossos serviços!')
