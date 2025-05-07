cadastro = dict()
pessoas = list()

condicao = 's'
idades = 0
mulheres = list()
maiores = list()

while condicao != 'n':
	cadastro.clear()
	cadastro['nome'] = input('Nome: ')
	while True:
		cadastro['sexo'] = input('Sexo: [M/F] ').upper()[0]
		#Pegará so a primeira letra do sexo.
		if cadastro['sexo'] in 'MF':
			break
		print('Erro! Digite apenas M ou F.')
	cadastro['idade'] = int(input('Idade: '))
	idades += cadastro['idade']
	pessoas.append(cadastro.copy())
	condicao = input('Quer continuar? [S/N] ').lower()[0]
	while True:
		if condicao in 'SNsn':
			break
		print('Erro! Responda apenas S ou N')
		condicao = input('Quer continuar? [S/N] ').lower()[0]

media = idades / len(pessoas)
print(f'\nA) Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'B) A média de idade é de {media} anos.')

for i in range(0, len(pessoas)):
	if pessoas[i]['sexo'] in 'Ff':
		mulheres.append(pessoas[i]['nome'])

print('C) As mulheres cadastradas foram: ', end=' ')
for i in range(0, len(mulheres)):
	print(f'{mulheres[i]}',end=' ')

for i in range(0, len(pessoas)):
	if pessoas[i]['idade'] > media:
		maiores.append(pessoas[i]['nome'])

print('\nD) As pessoas com idade acima da média são: ', end=' ')
for i in range(0, len(maiores)):
	print(f'{maiores[i]}',end=' ')
