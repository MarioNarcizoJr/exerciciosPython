itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 7.50)

print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<40}', end='')
    else:
        print(f'R${itens[pos]:>7}')

print('-'*50)
