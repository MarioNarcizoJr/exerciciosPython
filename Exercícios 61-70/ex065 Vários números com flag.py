numero = int(input('Digite um número [999 para parar]: '))
soma = 0
qtd = 0

while numero != 999:
    soma += numero
    qtd += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'\nA soma dos {qtd} números é igual a {soma}.')

