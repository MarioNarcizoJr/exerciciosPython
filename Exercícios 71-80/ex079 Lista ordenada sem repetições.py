valores = []
for i in range(0, 5):
    valor = int(input('Digite um número: '))
    valores.append(valor)
    valores.sort()
    if i == 0:
        print(f'O número {valor} foi adicionado na posição 0.')
    else:
        print(f'O número {valor} foi adicionado na posição {valores.index(valor)}')

print(f'\nA lista ficou da seguinte maneira: {valores}.')

