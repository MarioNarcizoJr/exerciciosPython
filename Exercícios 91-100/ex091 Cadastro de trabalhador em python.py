import datetime
cadastro = dict()
hoje = datetime.date.today().year

cadastro['nome'] = input('Nome: ')
cadastro['ano'] = int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratacao'] + 35) - cadastro['ano']
    print(f'\nMuito prazer, {cadastro["nome"]}.')
    print(f'Idade: {hoje - cadastro["ano"]} anos.')
    print(f'Ctps: {cadastro["ctps"]}.')
    print(f'Foi contratado em {cadastro["contratacao"]}.')
    print(f'Salário: R${cadastro["salario"]}.')
    print(f'Você se aposentará com {cadastro["aposentadoria"]} anos.')
else:
	print(f'\nMuito prazer, {cadastro["nome"]}.')
	print(f'Idade: {hoje - cadastro["ano"]} anos.')
	print(f'Ctps: {cadastro["ctps"]}.')


print('\nObrigado por utilizar nossos serviços.')