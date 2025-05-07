qtd = 0
soma = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        qtd = qtd + 1
        soma = soma + numero

print(f'A soma de {qtd} números ímpares múltiplos de 3 é igual a {soma}.')
