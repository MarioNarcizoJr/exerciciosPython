numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print('\nOs valores da tupla são:', numeros)
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'\nO primeiro valor 3 está na posição {numeros.index(3)}º.')
else:
    print('\nO valor 3 não aparece na tupla.')

print('\nNúmero(os) par(es): ', end= '')
for i in range(0,4):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')

print('\nFIM!')