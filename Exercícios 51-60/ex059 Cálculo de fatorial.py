numero = int(input('Digite o número para saber o fatorial dele: '))
cont = 1
print(f'\nFatorial de {numero}! igual a: ', end='')

while numero != 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    cont *= numero
    numero -= 1
print(cont)
