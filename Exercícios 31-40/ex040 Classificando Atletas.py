import datetime
nascimento = int(input('Digite o ano de seu nascimento: '))
atual = datetime.date.today().year
ano = atual - nascimento
if ano <= 9:
    print(f'Você tem {ano} anos e está na classe MIRIM.')
elif ano <= 14:
    print(f'Você tem {ano} anos e está na classe INFANTIL.')
elif ano <= 19:
    print(f'Você tem {ano} anos e está na classe JUNIOR.')
elif ano <= 25:
    print(f'Você tem {ano} anos e está na classe SÊNIOR.')
else:
    print(f'Você tem {ano} anos e está na classe MASTER.')
