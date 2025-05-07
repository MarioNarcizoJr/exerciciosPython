numeros = [[], []]

for i in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(f'\nOs números pares foram: {numeros[0]}.')
print(f'Os números ímpares foram: {numeros[1]}.')
