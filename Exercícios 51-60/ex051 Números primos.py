numero = int(input('Digite um número: '))
cont = 0
for contador in range(2, numero + 1):
    if numero % contador == 0:
        cont += 1

if cont == 1:
    print(f'O número {numero} É PRIMO.')
else:
    print(f'O número {numero} NÃO É PRIMO.')
