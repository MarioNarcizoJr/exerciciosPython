numero = int(input('Digite um número: '))
resposta = input('Deseja continuar [S/N]: ')
qtd = 1
soma = numero
maior = menor = numero

while resposta in 'sS':
    numero = int(input('Digite um número: '))
    qtd += 1
    soma += numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    resposta = input('Deseja continuar [S/N]: ')

print(f'Você digitou {qtd} números e a média entre eles é de {soma/qtd}.\nO maior Valor entre eles é de {maior} e o menor {menor}.')
