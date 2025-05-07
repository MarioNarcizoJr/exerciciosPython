import datetime
ano = int(input('Digite o ano que deseja | Digite 0 caso queira utilizar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0:
    print(f'O ano de {ano} É bissexto.')
else:
    print(f'O ano de {ano} NÃO é bissexto.')
