idade = 0
sexo = ''
opcao = ''
maiores = homem = mulher = 0

while opcao in 'sS':
    print('-='*12)
    print('CADASTRO DE UMA PESSOA')
    print('-=' * 12)
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ')
    if idade >= 18:
        maiores += 1
    if sexo in 'mM':
        homem += 1
    if sexo in 'fF' and idade < 20:
        mulher += 1
    opcao = input('\nQuer cadastrar outra pessoa? [S/N]: ')
print(f'Total de pessoas com mais de 18 anos: {maiores}.\n'
      f'Total de homens: {homem}.\n'
      f'Total de mulheres com menos de 20 anos: {mulher}.')
