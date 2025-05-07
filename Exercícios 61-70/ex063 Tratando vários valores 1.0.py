numero = int(input('Digite um número [999 p/ parar]: '))
qtd = 0
soma = 0
while numero != 999:
    soma += numero
    qtd += 1
    numero = int(input('Digite um número [999 p/ parar]: '))
print(f'Você digitou {qtd} números e a soma é {soma}.\nFim!')