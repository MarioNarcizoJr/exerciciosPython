import datetime
maiorid = menorid = ano = 0
anoatual = datetime.date.today().year
for pessoa in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pessoa}º pessoa: '))
    pessoa += 1
    if (anoatual - ano) >= 18:
        maiorid += 1
    else:
        menorid += 1
print(f'Foram registradas {maiorid} pessoas maiores de idade e {menorid} pessoas menores de idade.')
