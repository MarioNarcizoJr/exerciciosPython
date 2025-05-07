print('='*50)
print('{:^50}'.format('Banco Vivaldi'))
print('='*50)

valor = int(input('Digite o valor a ser sacado: '))

while valor > 0:
    if valor > 50:
        print(f'Total de {valor//50} cédulas de R$50.00.')
        valor = valor - (valor//50)*50
    elif valor > 20:
        print(f'Total de {valor//20} cédulas de R$20.00.')
        valor = valor - (valor //20)*20
    elif valor > 10:
        print(f'Total de {valor//10} cédulas de R$10.00.')
        valor = valor - (valor // 10)*10
    elif valor < 10:
        print(f'Total de {valor} cédulas de R$1.00.')
        valor -= valor
