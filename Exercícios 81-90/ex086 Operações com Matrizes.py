matriz = []

pares = valor = soma = maior = 0

for i in range(0, 9):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        pares += valor
    if len(matriz) == 3:
        maior = valor
    if len(matriz) == 4 or len(matriz) == 5:
        if valor > maior:
            maior = valor
    if len(matriz) == 6 or len(matriz) == 7 or len(matriz) == 8:
        soma += valor
    matriz.append(valor)

print(f'''\n[ {matriz[0]:>2} ]  [ {matriz[1]:>2} ]  [ {matriz[2]:>2} ]
[ {matriz[3]:>2} ]  [ {matriz[4]:>2} ]  [ {matriz[5]:>2} ]
[ {matriz[6]:>2} ]  [ {matriz[7]:>2} ]  [ {matriz[8]:>2} ]''')

print(f'\nA soma dos números pares é igual a : {pares}.'
      f'\nA soma da terceira coluna é igual a: {soma}.'
      f'\nO maior valor da segunda coluna é: {maior}')