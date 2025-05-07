import datetime
nascimento = int(input('Digite o ano de seu nascimento: '))
atual = datetime.date.today().year
if (atual - nascimento) > 18:
    print(f'Em {atual} você tem {atual - nascimento} anos,'
          f' já passou da hora de você se alistar, ano de alistamento: {atual-((atual-nascimento)-18)}.')
elif (atual - nascimento) == 18:
    print(f'Atenção, compareça imediatamente a autoridade militar de sua cidade, chegou sua vez!')
else:
    print(f'Calma garoto, você ainda tem {(atual-nascimento)} anos, seu alistamento será no ano de {atual + (18 - (atual-nascimento))}')
