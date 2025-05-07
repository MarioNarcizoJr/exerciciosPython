def maior(*num):
    maiorv = cont = 0
    print('\nAnalisando os valores passados: ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maiorv = valor
        else:
            if valor > maiorv:
                maiorv = valor
        cont += 1
    print(f'\nO maior valor foi: {maiorv}.')


maior(2, 5, 6, 8, 9, 10, 1)
maior(1, 3, 5, 6, 8, 9, 1)
maior(3, 5, 6, 7, 8, 1)
maior(1, 2, 6, 7, 1)
maior(1, 5, 6, 1)
maior(5, 11, 1)
