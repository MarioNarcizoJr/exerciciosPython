valores = []

valor = int(input('Digite um valor para a lista: '))
valores.append(valor)
condicao = input('\nDeseja adicionar mais algum valor [s/n]: ').lower()

while condicao not in 'n':
    valor = int(input('\nDigite um valor para a lista: '))
    if valor in valores:
        print('\nEste número ja foi adicionado na lista, por favor digite outro.')
    else:
        valores.append(valor)
    condicao = input('\nDeseja adicionar mais algum valor [s/n]: ').lower()

print()
print('='*50)
valores.sort()
print(f'\nVocê digitou os valors: {valores}')