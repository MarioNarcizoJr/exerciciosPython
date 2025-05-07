valores = []

valor = int(input('Digite um número: '))
valores.append(valor)
condicao = input('Deseja continuar? [S/N] ').lower()
contador = 1

while condicao != 'n':
    valor = int(input('Digite um número: '))
    valores.append(valor)
    condicao = input('Deseja continuar? [S/N] ').lower()
    contador += 1

print(f'\nVocê digitou {contador} elementos para a lista.')

valores.sort(reverse=True)
print(valores)

if 5 in valores:
    print('O número 5 ESTÁ presente na lista.')
else:
    print('O número 5 NÃO está presente na lista.')
