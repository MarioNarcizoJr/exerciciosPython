valores = []
pares = []
impares = []

valor = int(input('Digite um valor: '))
condicao = input('Deseja adicionar mais algum número?[S/N] ').lower()
valores.append(valor)

while condicao != 'n':
    valor = int(input('Digite um valor: '))
    condicao = input('Deseja adicionar mais algum número?[S/N] ').lower()
    valores.append(valor)

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])

print(f'\nA lista completa foi: {valores}.')
print(f'Só os números pares: {pares}.')
print(f'Só os números impares: {impares}.')