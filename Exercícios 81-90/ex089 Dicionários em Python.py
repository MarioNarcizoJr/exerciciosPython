alunos = dict()
alunos['Nome'] = input('Nome: ')
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
print(f'O nome é igual a {alunos["Nome"]}.')
print(f'A média é igual a: {alunos["Média"]}.')
if alunos['Média'] >=7:
	print('Situação é igual a Aprovado.')
else:
	print('Situação é igual a Reprovado.')