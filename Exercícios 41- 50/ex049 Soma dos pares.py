numero = 0
soma = 0
pares = 0
for variavel in range(0,6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = soma + numero
        pares = pares + 1
print(f'Você informou {pares} números pares, soma deles é igual a {soma}.')