def LeiaInt(x):
    x = input('Digite um número inteiro: ')
    if x.isnumeric():
        condicao = True
    else:
        condicao = False
    while not condicao:
        print('\033[0;31mValor atribuido INVÁLIDO, digite novamente!\033[m')
        x = input('Digite um número inteiro: ')
        condicao = x.isnumeric()
    return f'\033[0;32mO número digitado foi: {x}\033[m'


numero = LeiaInt('Digite um número: ')
print(numero)